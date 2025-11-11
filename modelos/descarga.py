from sqlalchemy import Column, Integer, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Descarga(Base):
    __tablename__ = 'descarga'

    id = Column(Integer, primary_key=True)
    fecha_descarga = Column(DateTime, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_libro = Column(Integer, ForeignKey('libros.id'), nullable=False)

