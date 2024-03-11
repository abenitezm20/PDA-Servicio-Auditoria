from src.auditoria.modulos.auditoria.dominio.entidades import Propiedad
from src.auditoria.modulos.auditoria.dominio.eventos import PropiedadRegistrada
from src.auditoria.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from src.auditoria.modulos.auditoria.infraestructura.repositorios import RepositorioPropiedadSQL
from src.auditoria.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from src.auditoria.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from src.auditoria.modulos.auditoria.infraestructura.despachadores import Despachador
from abc import ABC, abstractmethod
import traceback
import time


class ProyeccionPropiedad(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...


class ProyeccionRegistrarPropiedad(ProyeccionPropiedad):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, operacion, nombre, coordenadas, direccion, fecha_creacion):
        self.operacion = operacion
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.direccion = direccion
        self.fecha_creacion = fecha_creacion

    def ejecutar(self, db=None):
        if not db:
            print('ERROR: DB del app no puede ser nula')
            return

        print('Ejecutando proyección de catastro...')
        time.sleep(10)
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(
            RepositorioPropiedadSQL.__class__)
        repositorio.agregar(
            Propiedad(nombre=self.nombre,
                              coordenadas=self.coordenadas,
                              direccion=self.direccion,
                              fecha_creacion=self.fecha_creacion))
        db.commit()

        evento = PropiedadRegistrada(propiedad_id=self.id,
                                             nombre=self.nombre,
                                             coordenadas=self.coordenadas,
                                             direccion=self.direccion,
                                             fecha_creacion=self.fecha_creacion)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria')
        print('Proyección de auditoria ejecutada!')




class ProyeccionPropiedadHandler(ProyeccionHandler):

    def handle(self, proyeccion: ProyeccionPropiedad):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from src.auditoria.conf.db import db_session as db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionRegistrarPropiedad)
def ejecutar_proyeccion_propiedad(proyeccion, app=None):
    if not app:
        print('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionPropiedadHandler()
            handler.handle(proyeccion)

    except:
        traceback.print_exc()
        print('ERROR: Persistiendo!')