from src.auditoria.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class Propiedad(Base):
    __tablename__ = "propiedad"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    coordenadas = Column(String)
    direccion = Column(String)
    fecha_creacion = Column(String)
    fecha_actualizacion = Column(String)
    propiedad_id = Column(String)

    def __init__(self, nombre, coordenadas, direccion, fecha_creacion, propiedad_id):
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.direccion = direccion
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_creacion
        self.propiedad_id = propiedad_id