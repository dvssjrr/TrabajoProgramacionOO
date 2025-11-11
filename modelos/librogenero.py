from sqlalchemy import Column, ForeignKey, Integer
from .base import Base

class LibroGenero(Base):
    __tablename__ = 'libro_genero'

    id_libro = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    id_genero = Column(Integer, ForeignKey('generos.id'), primary_key=True)