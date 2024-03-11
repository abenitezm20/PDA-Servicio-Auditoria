from src.auditoria.seedwork.aplicacion.dto import DTO, Mapeador as AppMap
from src.auditoria.seedwork.dominio.repositorios import Mapeador as RepMap
from src.auditoria.modulos.auditoria.aplicacion.dto import PropiedadDTO
from src.auditoria.modulos.auditoria.dominio.entidades import Propiedad

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO
        propiedad_dto.nombre = externo.get('nombre')
        propiedad_dto.coordenadas = externo.get('coordenadas')
        propiedad_dto.direccion = externo.get('direccion')
        propiedad_dto.fecha_creacion = externo.get('fecha_creacion')
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__


class MapeadorPropiedad(RepMap):
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        entidad = Propiedad()
        entidad.nombre = dto.nombre
        entidad.coordenadas = dto.coordenadas
        entidad.direccion = dto.direccion
        entidad.fecha_creacion = dto.fecha_creacion
        return entidad
    
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        dto = PropiedadDTO(
            entidad.nombre,
            entidad.coordenadas,
            entidad.direccion,
            entidad.fecha_creacion
        )
        return dto
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__