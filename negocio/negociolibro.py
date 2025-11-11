from datos import obtener_lista_objetos, crear_objeto, modificar_objeto
from iu import (
    str_isbn_libro, str_titulo_libro, str_año_publicacion_libro, 
    str_nuevo_isbn_libro, str_nuevo_titulo_libro, str_nuevo_año_publicacion_libro
)
from modelos import Libro
from prettytable import PrettyTable


def obtener_listado_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['N', 'ISBN', 'Titulo', 'Anio Pub.', 'Copias Disp.', 'Habilitado']
    lista_libros = obtener_lista_objetos(Libro)
    
    if lista_libros:
        for libro in lista_libros:
            estado = 'Si' if libro.habilitado == 1 else 'No'
            tabla_libros.add_row(
                [libro.id, libro.isbn, libro.titulo, libro.año_publicacion, libro.copias_disponibles, estado]
            )
    
    print(tabla_libros)


def obtener_libro_por_isbn(isbn: str):
    lista_libros = obtener_lista_objetos(Libro)
    if lista_libros:
        for libro in lista_libros:
            if libro.isbn == isbn:
                return libro
    return None


def crear_libro():
    isbn = str_isbn_libro()
    
    if isbn != '':
        libro_existente = obtener_libro_por_isbn(isbn)
        
        if libro_existente is None:
            titulo = str_titulo_libro()
            año_publicacion = str_año_publicacion_libro()
            
            nuevo_libro = Libro(
                isbn=isbn,
                titulo=titulo.title(),
                año_publicacion=año_publicacion,
            )
            crear_objeto(nuevo_libro)
            print(f'Libro "{titulo.title()}" (ISBN: {isbn}) creado con exito.')
        else:
            print('Este libro ya EXISTE (ISBN duplicado).')

def modificar_libro():
    isbn = str_isbn_libro()
    
    if isbn != '':
        libro = obtener_libro_por_isbn(isbn)
        
        if libro:
            modificar_isbn = str_nuevo_isbn_libro()
            modificar_titulo = str_nuevo_titulo_libro()
            modificar_anio = str_nuevo_año_publicacion_libro()
            
            if modificar_isbn != '':
                libro.isbn = modificar_isbn
                
            if modificar_titulo != '':
                libro.titulo = modificar_titulo.title()
            
            if modificar_anio != '':
                libro.anio_publicacion = modificar_anio
            
            modificar_objeto(libro)
            print(f'Libro "{libro.titulo}" modificado con exito.')
            
        else:
            print('No se ha encontrado el libro con ese ISBN.')