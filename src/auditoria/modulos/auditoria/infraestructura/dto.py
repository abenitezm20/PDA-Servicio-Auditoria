from src.auditoria.conf.db import Base
from sqlalchemy import Column, String, DateTime, Integer

class Propiedad(Base):
    __tablename__ = "propiedad"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    coordenadas = Column(String)
    direccion = Column(String)
    fecha_creacion = Column(String)

    def __init__(self, nombre, coordenadas, direccion, fecha_creacion):
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.direccion = direccion
        self.fecha_creacion = fecha_creacion