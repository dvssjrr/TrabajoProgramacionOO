from .obtenerdatos import (
    obtener_lista_objetos,
    obtener_lista_libros,
    obtener_lista_autores,
    obtener_lista_clientes,
    modificar_objeto
)
from .guardar_datos import (
    crear_objeto,
    guardar_autor,
    guardar_libro
)
from .eliminar_datos import eliminar_objeto

__all__ = [
    "obtener_lista_objetos",
    "obtener_lista_libros",
    "obtener_lista_autores",
    "obtener_lista_clientes",
    "crear_objeto",
    "modificar_objeto",
    "guardar_autor",
    "guardar_libro",
    "eliminar_objeto",
]
