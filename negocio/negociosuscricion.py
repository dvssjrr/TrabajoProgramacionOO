from prettytable import PrettyTable
from datos import obtener_lista_objetos, crear_objeto, modificar_objeto, eliminar_objeto

def obtener_listado_tipos_suscripcion():
    try:
        from modelos import TipoSuscripcion
    except Exception:
        print("Tipos de suscripción: funcionalidad pendiente (modelo TipoSuscripcion no definido).")
        return

    tabla_suscripciones = PrettyTable()
    tabla_suscripciones.field_names = ['N°', 'Nombre Plan', 'Límite Libros', 'Días Préstamo', 'Costo Mensual']
    lista_tipos = obtener_lista_objetos(TipoSuscripcion)
    
    if lista_tipos:
        for tipo in lista_tipos:
            costo = getattr(tipo, 'costo_mensual', 'N/A')
            tabla_suscripciones.add_row(
                [tipo.id, tipo.nombre_suscripcion, tipo.limite_libros, tipo.dias_prestamo, costo])
    
    print(tabla_suscripciones)

def obtener_tipo_suscripcion_nombre(nombre: str):
    nombre_normalizado = nombre.title()
    try:
        from modelos import TipoSuscripcion
    except Exception:
        return None

    lista_tipos = obtener_lista_objetos(TipoSuscripcion)
    if lista_tipos:
        for tipo in lista_tipos:
            if tipo.nombre_suscripcion == nombre_normalizado:
                return tipo
    return None

def crear_tipo_suscripcion():
    nombre = input('Ingrese nombre del tipo de suscripción (vacío para cancelar): ').strip()
    
    if nombre:
        nombre_normalizado = nombre.title()
        tipo_existente = obtener_tipo_suscripcion_nombre(nombre_normalizado)
        
        if tipo_existente is None:
            limite_libros = input('Ingrese límite de libros: ').strip()
            dias_prestamo = input('Ingrese días de préstamo: ').strip()
            costo_mensual = input('Ingrese costo mensual: ').strip()
            try:
                from modelos import TipoSuscripcion
                nuevo_tipo = TipoSuscripcion(
                    nombre_suscripcion=nombre_normalizado,
                    limite_libros=int(limite_libros) if limite_libros else None,
                    dias_prestamo=int(dias_prestamo) if dias_prestamo else None,
                    costo_mensual=float(costo_mensual) if costo_mensual else 0.0
                )
                crear_objeto(nuevo_tipo)
                print(f'Tipo de Suscripción "{nombre_normalizado}" creado con éxito.')
            except Exception:
                print(f'No es posible crear el plan: modelo TipoSuscripcion no definido en el proyecto.')
        else:
            print(f'Este plan de suscripción "{nombre_normalizado}" ya EXISTE.')
    else:
        print('Operación cancelada: El nombre del plan no puede estar vacío.')

def modificar_tipo_suscripcion():
    nombre_actual = input('Ingrese nombre del plan a modificar (vacío para cancelar): ').strip()
    
    if not nombre_actual:
        print('Operación cancelada: El nombre del plan a modificar no puede estar vacío.')
        return
    
    tipo = obtener_tipo_suscripcion_nombre(nombre_actual)
    
    if tipo is None:
        print(f'No se ha encontrado el plan de suscripción con nombre "{nombre_actual}".')
        return
    
    print(f'Modificando plan: "{tipo.nombre_suscripcion}"')
    
    modificar_nombre = input('Nuevo nombre (vacío para mantener): ').strip()
    modificar_limite = input('Nuevo límite libros (vacío para mantener): ').strip()
    modificar_dias = input('Nuevos días préstamo (vacío para mantener): ').strip()
    
    if modificar_nombre:
        tipo.nombre_suscripcion = modificar_nombre.title()
    if modificar_limite:
        try:
            tipo.limite_libros = int(modificar_limite)
        except ValueError:
            print('Límite de libros inválido, se mantiene el anterior.')
    if modificar_dias:
        try:
            tipo.dias_prestamo = int(modificar_dias)
        except ValueError:
            print('Días de préstamo inválido, se mantiene el anterior.')
    
    try:
        modificar_objeto(tipo)
        print('Plan modificado con éxito.')
    except Exception:
        print('No fue posible modificar el plan (modelo o persistencia no disponible).')

def eliminar_tipo_suscripcion():
    nombre = input("Ingrese el nombre del plan a eliminar (vacío para cancelar): ").strip()

    if not nombre:
        print("Operación cancelada.")
        return

    tipo = obtener_tipo_suscripcion_nombre(nombre)

    if tipo is None:
        print(f'No se encontró un plan con el nombre "{nombre}".')
        return

    print(f'Plan encontrado: {tipo.nombre_suscripcion}')
    confirmacion = input("¿Está seguro que desea ELIMINAR este plan? (s/n): ").strip().lower()

    if confirmacion == 's':
        try:
            eliminar_objeto(tipo)
            print(f'El plan "{tipo.nombre_suscripcion}" ha sido eliminado correctamente.')
        except Exception as e:
            print("Error al eliminar el plan:", e)
    else:
        print("Operación cancelada.")
