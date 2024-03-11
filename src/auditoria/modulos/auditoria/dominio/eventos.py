from __future__ import annotations
from dataclasses import dataclass
from src.auditoria.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class PropiedadRegistrada(EventoDominio):
    id: int = None
    nombre: str = None
    coordenadas: str = None
    direccion: str = None
    fecha_creacion: str = None
