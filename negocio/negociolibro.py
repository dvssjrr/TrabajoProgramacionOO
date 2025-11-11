from datos import obtener_lista_objetos, crear_objeto, modificar_objeto
from modelos import Libro
from prettytable import PrettyTable


def obtener_listado_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['N', 'ISBN', 'Titulo', 'Anio Pub.', 'Copias Disp.', 'Habilitado']
    lista_libros = obtener_lista_objetos(Libro)
    
    if lista_libros:
        for libro in lista_libros:
            estado = 'Si' if getattr(libro, 'habilitado', 1) == 1 else 'No'
            tabla_libros.add_row(
                [libro.id, libro.isbn, libro.titulo, getattr(libro, 'anio_publicacion', ''), libro.copias_disponibles, estado]
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
    isbn = input('Ingrese ISBN del libro (vacío para cancelar): ').strip()
    
    if isbn != '':
        libro_existente = obtener_libro_por_isbn(isbn)
        
        if libro_existente is None:
            titulo = input('Ingrese titulo del libro: ').strip()
            anio_publicacion = input('Ingrese año de publicación (YYYY): ').strip()
            
            nuevo_libro = Libro(
                isbn=isbn,
                titulo=titulo.title(),
                anio_publicacion=anio_publicacion,
            )
            crear_objeto(nuevo_libro)
            print(f'Libro "{titulo.title()}" (ISBN: {isbn}) creado con exito.')
        else:
            print('Este libro ya EXISTE (ISBN duplicado).')

def modificar_libro():
    isbn = input('Ingrese ISBN del libro a modificar (vacío para cancelar): ').strip()
    
    if isbn != '':
        libro = obtener_libro_por_isbn(isbn)
        
        if libro:
            modificar_isbn = input('Nuevo ISBN (vacío para mantener): ').strip()
            modificar_titulo = input('Nuevo titulo (vacío para mantener): ').strip()
            modificar_anio = input('Nuevo año de publicación (YYYY) (vacío para mantener): ').strip()
            
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