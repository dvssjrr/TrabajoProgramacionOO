from datos import obtener_lista_objetos, crear_objeto, modificar_objeto
from iu import str_nombre_suscripcion, str_limite_libros, str_dias_prestamo, str_nuevo_nombre_suscripcion, str_nuevo_limite_libros, str_nuevo_dias_prestamo
from modelos import TipoSuscripcion
from prettytable import PrettyTable


def obtener_listado_tipos_suscripcion():
    tabla_suscripciones = PrettyTable()
    tabla_suscripciones.field_names = ['N°', 'Nombre Plan', 'Límite Libros', 'Días Préstamo', 'Costo Mensual']
    lista_tipos = obtener_lista_objetos(TipoSuscripcion)
    
    if lista_tipos:
        for tipo in lista_tipos:
            tabla_suscripciones.add_row(
                [tipo.id, tipo.nombre_suscripcion, tipo.limite_libros, tipo.dias_prestamo, tipo.costo_mensual])
    
    print(tabla_suscripciones)


def obtener_tipo_suscripcion_nombre(nombre: str):
    lista_tipos = obtener_lista_objetos(TipoSuscripcion)
    if lista_tipos:
        for tipo in lista_tipos:
            if tipo.nombre_suscripcion == nombre.title():
                return tipo
    return None


def crear_tipo_suscripcion():
    nombre = str_nombre_suscripcion()
    
    if nombre != '':
        tipo_existente = obtener_tipo_suscripcion_nombre(nombre)
        
        if tipo_existente is None:
            limite_libros = str_limite_libros()
            dias_prestamo = str_dias_prestamo()
            
            nuevo_tipo = TipoSuscripcion(
                nombre_suscripcion=nombre.title(),
                limite_libros=limite_libros,
                dias_prestamo=dias_prestamo
            )
            crear_objeto(nuevo_tipo)
            print(f'Tipo de Suscripción "{nombre.title()}" creado con éxito.')
        else:
            print('Este plan de suscripción ya EXISTE.')

def modificar_tipo_suscripcion():
    nombre = str_nombre_suscripcion()
    
    if nombre != '':
        tipo = obtener_tipo_suscripcion_nombre(nombre)
        
        if tipo:
            modificar_nombre = str_nuevo_nombre_suscripcion()
            modificar_limite = str_nuevo_limite_libros()
            modificar_dias = str_nuevo_dias_prestamo()
            
            if modificar_nombre != '':
                tipo.nombre_suscripcion = modificar_nombre.title()
                
            if modificar_limite != '':
                try:
                    tipo.limite_libros = int(modificar_limite)
                except ValueError:
                    print('Límite de libros debe ser un número entero.')
                    return

            if modificar_dias != '':
                try:
                    tipo.dias_prestamo = int(modificar_dias)
                except ValueError:
                    print('Días de préstamo debe ser un número entero.')
                    return
            
            modificar_objeto(tipo)
            print(f'Plan "{nombre.title()}" modificado con éxito.')
            
        else:
            print('No se ha encontrado el plan de suscripción.')