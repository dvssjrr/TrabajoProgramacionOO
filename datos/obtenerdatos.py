from datos.conexion import Session
from sqlalchemy import func

from modelos.libro import Libro 
from modelos.autor import Autor
from modelos.cliente import Cliente

def modificar_objeto(objeto):
	sesion = Session()
	try:
		sesion.merge(objeto)
		sesion.commit()
		print("El objeto se ha modificado correctamente.")
	except Exception as e:
		sesion.rollback()
		print(f"Error al modificar el objeto: {e}")
	finally:
		sesion.close()
		
def obtener_lista_objetos(objeto):
	sesion = Session()
	try:
		listado_objetos = sesion.query(objeto).all()
		if len(listado_objetos) > 0:
			return listado_objetos
		return None
	finally:
		sesion.close()

def obtener_lista_libros(filtro):
	sesion = Session()
	try:
		busqueda = "%{}%".format(filtro)
		listado_objetos = sesion.query(Libro).filter(Libro.titulo.like(busqueda)).all()
		if len(listado_objetos) > 0:
			return listado_objetos
		return None
	finally:
		sesion.close()

def obtener_lista_autores(filtro):
	sesion = Session()
	try:
		busqueda = "%{}%".format(filtro)
		listado_objetos = (
			sesion.query(Autor)
			.filter(
				func.lower(Autor.nombre).like(func.lower(busqueda)) |
				func.lower(Autor.apellido).like(func.lower(busqueda))
			)
			.all()
		)
		
		if len(listado_objetos) > 0:
			return listado_objetos
		return None
	finally:
		sesion.close()

def obtener_lista_clientes(filtro):
	sesion = Session()
	try:
		busqueda = "%{}%".format(filtro)
		listado_objetos = sesion.query(Cliente).filter(Cliente.nombre_completo.like(busqueda)).all()
		
		if len(listado_objetos) > 0:
			return listado_objetos
		return None
	finally:
		sesion.close()