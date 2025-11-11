from sqlalchemy import Column, Integer, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LibroGenero(Base):
    __tablename__ = 'libro_genero'

    id_libro = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    id_genero = Column(Integer, ForeignKey('generos.id'), primary_key=True)