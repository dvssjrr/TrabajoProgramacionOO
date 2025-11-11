from sqlalchemy import Column, ForeignKey, Integer
from .base import Base

class LibroAutor(Base):
    __tablename__ = 'libro_autor'

    id_libro = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    id_autor = Column(Integer, ForeignKey('autores.id'), primary_key=True)