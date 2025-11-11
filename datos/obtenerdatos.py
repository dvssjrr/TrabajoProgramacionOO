from datos.conexion import Session
from sqlalchemy import func

from modelos.libro import Libro 
from modelos.autor import Autor
from modelos.cliente import Cliente

sesion = Session()


def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos
    return None

def obtener_lista_libros(filtro):
    busqueda = "%{}%".format(filtro)
    listado_objetos = sesion.query(Libro).filter(Libro.titulo.like(busqueda)).all()
    
    if len(listado_objetos) > 0:
        return listado_objetos
    return None

def obtener_lista_autores(filtro):
    busqueda = "%{}%".format(filtro)
    listado_objetos = (
        sesion.query(Autor)
        .filter(
            func.lower(Autor.nombre_autor).like(func.lower(busqueda)) |
            func.lower(Autor.apellido_autor).like(func.lower(busqueda))
        )
        .all()
    )
    
    if len(listado_objetos) > 0:
        return listado_objetos
    return None

def obtener_lista_clientes(filtro):
    busqueda = "%{}%".format(filtro)
    listado_objetos = sesion.query(Cliente).filter(Cliente.nombre_cliente.like(busqueda)).all()
    
    if len(listado_objetos) > 0:
        return listado_objetos
    return None