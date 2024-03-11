from flask import Flask, jsonify
from src.auditoria.conf.errors import ApiError
from src.auditoria.conf.db import init_db
from .auditoria import ba

app = Flask(__name__)
app.secret_key = '1D7FC7F9-3B7E-4C40-AF4D-141ED3F6013A'
init_db()
app.register_blueprint(ba)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "msg": err.description
    }
    return jsonify(response), err.code


def comenzar_consumidor():
    import threading
    import src.auditoria.modulos.auditoria.infraestructura.consumidores as auditoria

    # Suscripción a eventos
    threading.Thread(target=auditoria.suscribirse_a_eventos).start()
    threading.Thread(target=auditoria.suscribirse_a_eventos,
                     args=[app]).start()

    # Suscripción a comandos
    # threading.Thread(target=contratos.suscribirse_a_comandos).start()
    threading.Thread(target=auditoria.suscribirse_a_comandos,
                     args=[app]).start()


comenzar_consumidor()