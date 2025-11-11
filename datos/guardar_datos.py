from datos.conexion import Session
from sqlalchemy import func
from modelos.autor import Autor
from modelos.libro import Libro 

def crear_objeto(objeto):
	sesion = Session()
	try:
		sesion.add(objeto)
		sesion.commit()
		print("El objeto se ha guardado correctamente.")
	except Exception as e:
		sesion.rollback()
		print(f"Error al guardar el objeto: {e}")
	finally:
		sesion.close()

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

def guardar_autor(nombre, apellido, nacionalidad):
	if nombre != '' and apellido != '':
		sesion = Session()
		try:
			nuevo_autor = Autor(
				nombre=nombre,
				apellido=apellido,
				nacionalidad=nacionalidad.title()
			)
			sesion.add(nuevo_autor)
			sesion.commit()
			print(f"El Autor '{nuevo_autor.nombre} {nuevo_autor.apellido}' se ha registrado correctamente.")
		except Exception as e:
			sesion.rollback()
			print(f"Error al registrar el Autor: {e}")
		finally:
			sesion.close()
	else:
		print('Debe ingresar el nombre y el apellido del autor.')

def guardar_libro(titulo, isbn, anio_publicacion, copias_disponibles=0):
	if titulo != '' and isbn != '':
		sesion = Session()
		try:
			nuevo_libro = Libro(
				titulo=titulo,
				isbn=isbn,
				anio_publicacion=anio_publicacion,
				copias_disponibles=copias_disponibles
			)
			sesion.add(nuevo_libro)
			sesion.commit()
			print(f"El Libro '{nuevo_libro.titulo}' (ISBN: {nuevo_libro.isbn}) se ha guardado correctamente.")
		except Exception as e:
			sesion.rollback()
			print(f"Error al guardar el Libro: {e}")
		finally:
			sesion.close()
	else:
		print('Debe ingresar el título y el ISBN del libro.')