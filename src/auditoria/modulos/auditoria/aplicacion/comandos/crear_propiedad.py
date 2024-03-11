from dataclasses import dataclass
from src.auditoria.seedwork.aplicacion.comandos import Comando
from src.auditoria.seedwork.aplicacion.comandos import ejecutar_comando as comando
from src.auditoria.modulos.auditoria.aplicacion.dto import PropiedadDTO
from src.auditoria.modulos.auditoria.dominio.entidades import Propiedad
from src.auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorPropiedad
from src.auditoria.modulos.auditoria.infraestructura.repositorios import RepositorioPropiedadSQL
from src.auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .base import RegistrarPropiedadBaseHandler


@dataclass
class RegistrarPropiedad(Comando):
    nombre: str
    coordenadas: str
    direccion: str
    fecha_creacion: str


class RegistrarPropiedadHandler(RegistrarPropiedadBaseHandler):

    def handle(self, comando: RegistrarPropiedad):
        propiedad_dto = PropiedadDTO(
            nombre=comando.nombre,
            coordenadas=comando.coordenadas,
            direccion=comando.direccion,
            fecha_craecion=comando.fecha_craecion,
        )

        propiedad: Propiedad = self.fabrica_catastro.crear_objeto(
            propiedad_dto, MapeadorPropiedad())
        propiedad.registrar_propiedad(propiedad)
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedadSQL.__class__)

        print('Registrando crear contrato en la unidad de trabajo')
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()


@comando.register(RegistrarPropiedad)
def ejecutar_comando_crear_propiedad(comando: RegistrarPropiedad):
    print('Registrando comando crear propiedad')
    handler = RegistrarPropiedadHandler()
    handler.handle(comando)
