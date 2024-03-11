from src.auditoria.seedwork.dominio.repositorios import Mapeador
from src.auditoria.modulos.auditoria.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedad(Mapeador):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(
            entidad.id,
            entidad.nombre,
            entidad.coordenadas,
            entidad.direccion,
            entidad.fecha_creacion
        )

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            nombre=dto.nombre,
            coordenadas=dto.coordenadas,
            direccion=dto.direccion,
            fecha_creacion=dto.fecha_creacion,
        )
        
        return propiedad