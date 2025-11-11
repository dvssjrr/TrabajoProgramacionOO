from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prestamo(Base):
    __tablename__ = 'prestamos'

    id = Column(Integer, primary_key=True)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion_limite = Column(DateTime, nullable=False)
    fecha_devolucion_real = Column(DateTime, nullable=True)
    multa_total = Column(Float, default=0.00, nullable=True)
    devuelto = Column(Integer, default=0, nullable=False)

    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_libro = Column(Integer, ForeignKey('libros.id'), nullable=False)
    id_bibliotecario = Column(Integer, ForeignKey('usuario.id'), nullable=True)