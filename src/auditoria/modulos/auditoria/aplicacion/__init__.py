from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from src.auditoria.modulos.auditoria.dominio.eventos import PropiedadRegistrada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada,
                   signal=f'{PropiedadRegistrada.__name__}Integracion')
