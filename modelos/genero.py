from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class declarative_base:
    __tablename__ = 'generos'
    
    id = Column(Integer, primary_key=True)
    nombre_genero = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)

    libros = relationship("Libro", secondary="libro_genero", back_populates="generos")