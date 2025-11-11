from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class LibroAutor(Base):
    __tablename__ = 'libro_autor'
    
    id_libro = Column(Integer, ForeignKey('libros.id'), primary_key=True)
    id_autor = Column(Integer, ForeignKey('autores.id'), primary_key=True)