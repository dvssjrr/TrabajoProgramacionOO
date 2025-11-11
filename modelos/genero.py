from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genero(Base):
    __tablename__ = 'generos'
    
    id = Column(Integer, primary_key=True)
    nombre_genero = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)
