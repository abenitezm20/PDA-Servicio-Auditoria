from flask import Blueprint, Response, request
from auditoria.modulos.auditoria.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from auditoria.modulos.auditoria.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from auditoria.seedwork.aplicacion.queries import ejecutar_query

from auditoria.modulos.auditoria.infraestructura.despachadores import Despachador

ba = Blueprint('auditoria', __name__)

@ba.route('/auditoria/health', methods = ['GET'])
def health():
    return Response({'result': 'OK'})

@ba.route('/auditoria/propiedad/<id>', methods = ['GET'])
def obtener_propiedad(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_catastro = MapeadorPropiedadDTOJson()
        return map_catastro.dto_a_externo(query_resultado.resultado)
    else:
        return Response({'message': 'GET'})

@ba.route('/auditoria/propiedad', methods=['POST'])
def registrar_propiedad_async():
    map_propiedad = MapeadorPropiedadDTOJson()
    propiedad_dto = map_propiedad.externo_a_dto(request.json)

    Despachador().publicar_comando(propiedad_dto, 'comandos-auditoria')
    return Response('{}', status=202, mimetype='application/json')