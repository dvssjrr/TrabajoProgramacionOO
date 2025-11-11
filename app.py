from iu import menu_principal, menu_gestion_libros, menu_gestion_suscripcion, menu_gestion_clientes, menu_gestion_autores
from negocio import (
    obtener_listado_libros, crear_libro, modificar_libro, 
    obtener_listado_tipos_suscripcion, crear_tipo_suscripcion, modificar_tipo_suscripcion,
)
from auxiliares import nombre_aplicacion, numero_version

seleccionar_opcion = 'Seleccione su opcion [0-4]: '
opcion_incorrecta = 'Opcion Incorrecta, ingrese nuevamente...'
volver_menu_principal = 'Volviendo al menu principal...'

print(f'{nombre_aplicacion} {numero_version}')
while True:
    print()
    menu_principal()
    opcion = input('Seleccione su opcion [0-4]: ') # El menú principal ahora tiene opciones 1-4 y 0.
    
    # [1] Gestionar Libros
    if opcion == '1':
        while True:
            menu_gestion_libros()
            opcion_libro = input(seleccionar_opcion)
            
            if opcion_libro == '1':
                crear_libro()
            elif opcion_libro == '2':
                modificar_libro()
            elif opcion_libro == '3':
                print('Funcion para eliminar Libro (Pendiente)')
            elif opcion_libro == '4':
                obtener_listado_libros()
            elif opcion_libro == '0':
                print(volver_menu_principal)
                break
            else:
                print(opcion_incorrecta)
    
    # [2] Gestionar Suscripcion (Tipos de Suscripcion)
    elif opcion == '2':
        while True:
            menu_gestion_suscripcion()
            opcion_suscripcion = input(seleccionar_opcion)
            
            if opcion_suscripcion == '1':
                crear_tipo_suscripcion()
            elif opcion_suscripcion == '2':
                modificar_tipo_suscripcion()
            elif opcion_suscripcion == '3':
                print('Funcion para eliminar Suscripcion (Pendiente)')
            elif opcion_suscripcion == '4':
                obtener_listado_tipos_suscripcion()
            elif opcion_suscripcion == '0':
                print(volver_menu_principal)
                break
            else:
                print(opcion_incorrecta)

    # [3] Gestionar Clientes
    elif opcion == '3':
        while True:
            menu_gestion_clientes()
            opcion_cliente = input(seleccionar_opcion)
            
            if opcion_cliente == '1':
                print('Funcion para Registrar nuevo Cliente (Pendiente)')
            elif opcion_cliente == '2':
                print('Funcion para Modificar Cliente (Pendiente)')
            elif opcion_cliente == '3':
                print('Funcion para Eliminar Cliente (Pendiente)')
            elif opcion_cliente == '4':
                print('Funcion para Listar todos los Clientes (Pendiente)')
            elif opcion_cliente == '0':
                print(volver_menu_principal)
                break
            else:
                print(opcion_incorrecta)

    # [4] Gestionar Autores
    elif opcion == '4':
        while True:
            menu_gestion_autores()
            opcion_autor = input(seleccionar_opcion)
            
            if opcion_autor == '1':
                print('Funcion para Registrar nuevo Autor (Pendiente)')
            elif opcion_autor == '2':
                print('Funcion para Modificar Autor (Pendiente)')
            elif opcion_autor == '3':
                print('Funcion para Eliminar Autor (Pendiente)')
            elif opcion_autor == '4':
                print('Funcion para Listar todos los Autores (Pendiente)')
            elif opcion_autor == '0':
                print(volver_menu_principal)
                break
            else:
                print(opcion_incorrecta)

    # [0] Salir
    elif opcion == '0':
        print('Saliendo...')
        break
    
    else:
        print(opcion_incorrecta)