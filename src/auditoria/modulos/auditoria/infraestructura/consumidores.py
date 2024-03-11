import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback
from src.auditoria.modulos.auditoria.infraestructura.proyecciones import ProyeccionRegistrarPropiedad

from src.auditoria.modulos.auditoria.infraestructura.schema.v1.eventos import EventoRegistroPropiedadCreada
from src.auditoria.modulos.auditoria.infraestructura.schema.v1.comandos import ComandoRegistrarPropiedad
from src.auditoria.seedwork.infraestructura import utils

#from src.auditoria.modulos.auditoria.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from src.auditoria.seedwork.aplicacion.comandos import ejecutar_comando
from flask import session

from src.auditoria.seedwork.infraestructura.proyecciones import ejecutar_proyeccion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-eventos', schema=AvroSchema(EventoRegistroPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-auditoria', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoRegistrarPropiedad))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            ejecutar_proyeccion(ProyeccionRegistrarPropiedad(
                ProyeccionRegistrarPropiedad.ADD,
                mensaje.value().data.nombre,
                mensaje.value().data.coordenadas,
                mensaje.value().data.direccion,
                mensaje.value().data.fecha_creacion
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
