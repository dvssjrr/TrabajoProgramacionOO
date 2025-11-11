from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


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