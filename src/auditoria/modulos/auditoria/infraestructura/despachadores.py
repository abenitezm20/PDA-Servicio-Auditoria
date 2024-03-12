import pulsar
from pulsar.schema import *

from src.auditoria.modulos.auditoria.infraestructura.schema.v1.eventos import EventoRegistroPropiedadCreada,RegistroPropiedadPayload, EventoCrearPropiedadFallido, EventoCrearPropiedadFallidoPayload
from src.auditoria.modulos.auditoria.infraestructura.schema.v1.comandos import ComandoRegistrarPropiedad, ComandoRegistrarPropiedadPayload
from src.auditoria.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schemas):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(
            topico, schema=schemas)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = RegistroPropiedadPayload(
            id_propiedad=str(evento.propiedad_id),
            numero_contrato=str(11223344)
        )
        evento_integracion = EventoRegistroPropiedadCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoRegistroPropiedadCreada))

    def publicar_comando(self, dto, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        # if isinstance(comando, ComandoRegistrarArrendamiento):
        #     print('AQUI :)')
        payload = ComandoRegistrarPropiedadPayload(
            nombre=dto.nombre,
            coordenadas=dto.coordenadas,
            direccion=dto.direccion,
            fecha_creacion=dto.fecha_creacion,
        )

        comando_integracion = ComandoRegistrarPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico,
                               AvroSchema(ComandoRegistrarPropiedad))
        
    def publicar_compensacion(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = EventoCrearPropiedadFallidoPayload(
            id_propiedad=str(evento.propiedad_id)
        )
        evento_integracion = EventoCrearPropiedadFallido(data=payload)
        self._publicar_mensaje(evento_integracion, topico,
                               AvroSchema(EventoCrearPropiedadFallido))
    
