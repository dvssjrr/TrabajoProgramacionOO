from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Autor(Base):
	__tablename__ = 'autores'
	
	id = Column(Integer, primary_key=True)
	nombre = Column(String(100), nullable=False)
	apellido = Column(String(100), nullable=False)
	nacionalidad = Column(String(50), nullable=True)
	libros = relationship("Libro", secondary="libro_autor", back_populates="autores")