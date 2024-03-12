from pulsar.schema import *
from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class RegistroPropiedadPayload(Record):
    id_propiedad = String()
    numero_contrato = String()


class EventoRegistroPropiedadCreada(EventoIntegracion):
    data = RegistroPropiedadPayload()

class EventoCrearPropiedadFallidoPayload(Record):
    id_propiedad = String()

class EventoCrearPropiedadFallido(EventoIntegracion):
    data = EventoCrearPropiedadFallidoPayload()