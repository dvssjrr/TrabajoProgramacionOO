from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class declarative_base:
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True)
    isbn = Column(String(13), nullable=False, unique=True)
    titulo = Column(String(255), nullable=False)
    anio_publicacion = Column(String(4), nullable=True)
    editorial = Column(String(100), nullable=True)
    copias_disponibles = Column(Integer, default=0, nullable=False)
    habilitado = Column(Integer, default=1, nullable=False)