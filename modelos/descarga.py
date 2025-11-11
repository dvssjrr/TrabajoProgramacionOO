from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Descarga(Base):
    __tablename__ = 'descarga'
    
    id = Column(Integer, primary_key=True)
    fecha_descarga = Column(DateTime, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_libro = Column(Integer, ForeignKey('libros.id'), nullable=False)

    cliente = relationship("Cliente", back_populates="descargas")
    libro = relationship("Libro")
