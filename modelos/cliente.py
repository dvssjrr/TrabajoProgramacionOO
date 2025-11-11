from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True)
    rut_cliente = Column(String(15), nullable=True, unique=True)
    nombre_completo = Column(String(255), nullable=False)
    correo_contacto = Column(String(255), nullable=False, unique=True)
    telefono_contacto = Column(String(12), nullable=True)
    habilitado = Column(Integer, default=1, nullable=False)
    
    suscripcion = relationship("Suscripcion", back_populates="cliente", uselist=False)
    prestamos = relationship("Prestamo", back_populates="cliente")
    descargas = relationship("Descarga", back_populates="cliente")
    resenas = relationship("Resena", back_populates="cliente")