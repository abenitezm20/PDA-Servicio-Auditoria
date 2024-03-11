from pulsar.schema import *
from dataclasses import dataclass, field
from src.auditoria.seedwork.infraestructura.schema.v1.comandos import (
    ComandoIntegracion)


class ComandoRegistrarPropiedadPayload(Record):
    nombre = String()
    coordenadas = String()
    direccion = String()
    fecha_creacion = String()


class ComandoRegistrarPropiedad(ComandoIntegracion):
    data = ComandoRegistrarPropiedadPayload()
