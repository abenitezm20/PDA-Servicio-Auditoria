from .entidades import Propiedad
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadExcepcion
from src.auditoria.seedwork.dominio.repositorios import Mapeador
from src.auditoria.seedwork.dominio.fabricas import Fabrica
from src.auditoria.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad = mapeador.dto_a_entidad(obj)

            return propiedad

@dataclass
class FabricaPropiedad(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedad = _FabricaPropiedad()
            return fabrica_propiedad.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadExcepcion()