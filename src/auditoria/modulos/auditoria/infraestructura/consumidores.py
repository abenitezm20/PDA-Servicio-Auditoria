import pulsar
import _pulsar
from pulsar.schema import *
import logging
import traceback
from src.auditoria.modulos.auditoria.infraestructura.proyecciones import ProyeccionRegistrarPropiedad

from src.auditoria.modulos.auditoria.infraestructura.schema.v1.eventos import EventoRegistroPropiedadCreada, EventoCrearPropiedadFallido
from src.auditoria.modulos.auditoria.infraestructura.schema.v1.comandos import ComandoRegistrarPropiedad
from src.auditoria.seedwork.infraestructura import utils

#from src.auditoria.modulos.auditoria.aplicacion.comandos.crear_propiedad_contratos import RegistrarPropiedadContratos
from src.auditoria.seedwork.aplicacion.comandos import ejecutar_comando
from flask import session

from src.auditoria.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from datetime import datetime


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria-creada', consumer_type=_pulsar.ConsumerType.Shared,
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
        consumidor = cliente.subscribe('comandos-crear-auditoria', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoRegistrarPropiedad))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionRegistrarPropiedad(
                ProyeccionRegistrarPropiedad.ADD,
                nombre='casas rojas',
                coordenadas="{'lat':123, 'lng':456}",
                direccion='cll 127 N 32 - 43',
                fecha_creacion='2024-01-01',
                id_propiedad=mensaje.value().data.id_propiedad
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_compensacion(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-crear-propiedad-fallida', consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='pda-sub-comandos', schema=AvroSchema(EventoCrearPropiedadFallido))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando compensacion recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionRegistrarPropiedad(
                ProyeccionRegistrarPropiedad.DELETE,
                id_propiedad=mensaje.value().data.id_propiedad,
                fecha_creacion=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()