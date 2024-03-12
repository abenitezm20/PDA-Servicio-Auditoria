from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.entidades import AgregacionRaiz
from src.auditoria.modulos.auditoria.dominio.eventos import PropiedadRegistrada
import uuid

@dataclass
class Propiedad(AgregacionRaiz):
    nombre: str = field(default=str)
    coordenadas: str = field(default=str)
    direccion: str = field(default=str)
    fecha_creacion: str = field(default=str)
    fecha_actualizacion: str = field(default=str)
    propiedad_id: str = field(default=str)
    
    def registrar_propiedad(self, propiedad: Propiedad):

        self.agregar_evento(PropiedadRegistrada(
            propiedad_id=propiedad.propiedad_id,
            nombre=propiedad.nombre,
            coordenadas=propiedad.coordenadas,
            direccion=propiedad.direccion,
            fecha_creacion=propiedad.fecha_creacion))
