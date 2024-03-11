from dataclasses import dataclass, field
from src.auditoria.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    nombre: str = field(default_factory=str)
    coordenadas: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)