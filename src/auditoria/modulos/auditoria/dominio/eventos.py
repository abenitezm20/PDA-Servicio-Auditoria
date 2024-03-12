from __future__ import annotations
from dataclasses import dataclass
from src.auditoria.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PropiedadRegistrada(EventoDominio):
    propiedad_id: str = None
    nombre: str = None
    coordenadas: str = None
    direccion: str = None
    fecha_creacion: str = None
    fecha_actualizacion: str = None

@dataclass
class PropiedadAuditoriaReversada(EventoDominio):
    propiedad_id: str = None
