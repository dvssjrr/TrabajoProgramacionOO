from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from .base import Base

class Resena(Base):
    __tablename__ = 'reseña'

    id = Column(Integer, primary_key=True)
    calificacion = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=True)
    fecha_resena = Column(DateTime, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_libro = Column(Integer, ForeignKey('libros.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="resenas")
    libro = relationship("Libro")