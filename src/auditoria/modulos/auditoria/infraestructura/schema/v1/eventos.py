from pulsar.schema import *
from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroPropiedadPayload(Record):
    id_propiedad = String()


class EventoRegistroPropiedadCreada(EventoIntegracion):
    data = RegistroPropiedadPayload()
