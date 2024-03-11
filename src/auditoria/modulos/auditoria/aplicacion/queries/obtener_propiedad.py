from src.auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.auditoria.seedwork.aplicacion.queries import ejecutar_query as query
from src.auditoria.modulos.auditoria.infraestructura.repositorios import RepositorioPropiedadSQL
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from src.auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorPropiedad

@dataclass
class ObtenerPropiedad(Query):
    id: str

class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedadSQL.__class__)
        catastro =  self.fabrica_catastro.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=catastro)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)
