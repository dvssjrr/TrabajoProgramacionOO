from sqlalchemy import Column, Integer, String, Float
from modelos.base import Base

class TipoSuscripcion(Base):
    __tablename__ = 'tipos_suscripcion'

    id = Column(Integer, primary_key=True)
    nombre_suscripcion = Column(String(50), nullable=False, unique=True)
    limite_libros = Column(Integer, nullable=False, default=1)
    dias_prestamo = Column(Integer, nullable=False, default=7)
    costo_mensual = Column(Float, nullable=True)
