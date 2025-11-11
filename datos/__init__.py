from .obtenerdatos import (
    obtener_lista_objetos,
    obtener_lista_libros,
    obtener_lista_autores,
    obtener_lista_clientes,
    modificar_objeto as modificar_objeto_obtener
)
from .guardar_datos import (
    crear_objeto,
    modificar_objeto as modificar_objeto_guardar,
    guardar_autor,
    guardar_libro
)
from .eliminar_datos import eliminar_objeto

# Elegir la implementación por defecto para modificar_objeto (guardamos la de guardar_datos)
modificar_objeto = modificar_objeto_guardar

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