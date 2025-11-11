from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True)
    contrasena_hash = Column(String(255), nullable=False)
    es_admin = Column(Integer, default=0, nullable=False)
    habilitado = Column(Integer, default=1, nullable=False)

    prestamos_registrados = relationship("Prestamo", back_populates="bibliotecario")
