from sqlalchemy import Column, Integer, Date, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Suscripcion(Base):
	__tablename__ = 'suscripcion'
	
	id = Column(Integer, primary_key=True)
	fecha_inicio = Column(Date, nullable=False)
	fecha_fin = Column(Date, nullable=True)
	activa = Column(Integer, default=1, nullable=False)
	
	id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False, unique=True)
	id_tipo_suscripcion = Column(Integer, ForeignKey('tipos_suscripcion.id'), nullable=False)

	cliente = relationship("Cliente", back_populates="suscripcion")
	tipo = relationship("TipoSuscripcion", back_populates="suscripciones")