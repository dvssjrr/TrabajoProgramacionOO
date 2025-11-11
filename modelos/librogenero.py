from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class LibroGenero(Base):
    __tablename__ = 'libro_genero'
    
    id_libro = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    id_genero = Column(Integer, ForeignKey('generos.id'), primary_key=True)