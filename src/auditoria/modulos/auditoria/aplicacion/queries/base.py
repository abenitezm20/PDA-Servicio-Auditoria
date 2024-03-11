from src.auditoria.seedwork.aplicacion.queries import QueryHandler
from src.auditoria.modulos.auditoria.infraestructura.fabricas import FabricaRepositorio
from src.auditoria.modulos.auditoria.dominio.fabricas import FabricaPropiedad

class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_catastro: FabricaPropiedad = FabricaPropiedad()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_catastro(self):
        return self._fabrica_catastro    