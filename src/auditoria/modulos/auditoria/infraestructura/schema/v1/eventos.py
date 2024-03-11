from pulsar.schema import *
from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroPropiedadPayload(Record):
    id = String()
    nombre = String()
    coordenadas = String()
    direccion = String()
    fecha_creacion = String()


class EventoRegistroPropiedadCreada(EventoIntegracion):
    data = RegistroPropiedadPayload()
