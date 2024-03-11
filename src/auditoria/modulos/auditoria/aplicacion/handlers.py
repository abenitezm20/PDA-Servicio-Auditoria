from src.auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from src.auditoria.modulos.auditoria.aplicacion.comandos.crear_propiedad import RegistrarPropiedad
from src.auditoria.modulos.auditoria.infraestructura.despachadores import Despachador
from src.auditoria.seedwork.aplicacion.comandos import ejecutar_comando
from src.auditoria.seedwork.aplicacion.handlers import Handler
from datetime import datetime


class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria')


class HandlePropiedadDominio():
    @staticmethod
    def handle_propiedad_registrada(evento):
        obj = {
            "nombre": evento.nombre,
            "coordenadas": evento.coordenadas,
            "direccion": evento.direccion,
            "fecha_creacion": evento.fecha_creacion
        }
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(obj)
        comando = RegistrarPropiedad(
            propiedad_dto.nombre,
            propiedad_dto.coordenadas,
            propiedad_dto.direccion,
            propiedad_dto.fecha_creacion
        )

        ejecutar_comando(comando)
