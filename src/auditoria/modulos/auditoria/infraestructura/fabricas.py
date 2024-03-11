from dataclasses import dataclass
from src.auditoria.seedwork.dominio.fabricas import Fabrica
from src.auditoria.seedwork.dominio.repositorios import Repositorio
from src.auditoria.modulos.auditoria.dominio.repositorios import RepositorioPropiedad
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioPropiedadSQL

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedad.__class__:
            return RepositorioPropiedadSQL()
        else:
            raise ExcepcionFabrica()