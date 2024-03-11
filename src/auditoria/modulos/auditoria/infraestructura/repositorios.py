from src.auditoria.modulos.auditoria.dominio.repositorios import RepositorioPropiedad
from src.auditoria.modulos.auditoria.dominio.fabricas import FabricaPropiedad
from src.auditoria.modulos.auditoria.dominio.entidades import Propiedad
from uuid import UUID
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from src.auditoria.conf.db import db_session


class RepositorioPropiedadSQL(RepositorioPropiedad):

    def __init__(self):
        self._fabrica_propiedad: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_propiedad(self):
        return self._fabrica_propiedad

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db_session.query(PropiedadDTO).filter_by(propiedad_id=str(id)).one()
        return self._fabrica_propiedad.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        ...

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedad.crear_objeto(propiedad, MapeadorPropiedad())
        db_session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        ...

    def eliminar(self, propiedad_id: UUID):
        ...