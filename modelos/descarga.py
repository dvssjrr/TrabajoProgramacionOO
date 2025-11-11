from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .base import Base

class Descarga(Base):
    __tablename__ = 'descarga'

    id = Column(Integer, primary_key=True)
    fecha_descarga = Column(DateTime, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_libro = Column(Integer, ForeignKey('libros.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="descargas")
    libro = relationship("Libro")
