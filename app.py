from auxiliares import nombre_aplicacion, numero_version
from iu import menu_principal, menu_gestion_libros, menu_gestion_suscripcion, menu_gestion_clientes, menu_gestion_autores
from negocio import (
    obtener_listado_libros, crear_libro, modificar_libro,
    obtener_listado_tipos_suscripcion, crear_tipo_suscripcion, modificar_tipo_suscripcion,
)

seleccionar_opcion = 'Seleccione su opcion [0-4]: '
opcion_incorrecta = 'Opcion Incorrecta, ingrese nuevamente...'
volver_menu_principal = 'Volviendo al menu principal...'

print(f'{nombre_aplicacion} {numero_version}')

try:
    while True:
        print()
        menu_principal()
        opcion = input(seleccionar_opcion).strip()
        if opcion == '1':
            while True:
                menu_gestion_libros()
                opcion_libro = input(seleccionar_opcion).strip()
                if opcion_libro == '1':
                    crear_libro()
                elif opcion_libro == '2':
                    modificar_libro()
                elif opcion_libro == '3':
                    print('Eliminar Libro (Pendiente)')
                elif opcion_libro == '4':
                    obtener_listado_libros()
                elif opcion_libro == '0':
                    print(volver_menu_principal)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion == '2':
            while True:
                menu_gestion_suscripcion()
                opcion_suscripcion = input(seleccionar_opcion).strip()
                if opcion_suscripcion == '1':
                    crear_tipo_suscripcion()
                elif opcion_suscripcion == '2':
                    modificar_tipo_suscripcion()
                elif opcion_suscripcion == '3':
                    print('Eliminar Suscripcion (Pendiente)')
                elif opcion_suscripcion == '4':
                    obtener_listado_tipos_suscripcion()
                elif opcion_suscripcion == '0':
                    print(volver_menu_principal)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion == '3':
            while True:
                menu_gestion_clientes()
                opcion_cliente = input(seleccionar_opcion).strip()
                if opcion_cliente == '1':
                    print('Registrar nuevo Cliente (Pendiente)')
                elif opcion_cliente == '2':
                    print('Modificar Cliente (Pendiente)')
                elif opcion_cliente == '3':
                    print('Eliminar Cliente (Pendiente)')
                elif opcion_cliente == '4':
                    print('Listar todos los Clientes (Pendiente)')
                elif opcion_cliente == '0':
                    print(volver_menu_principal)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion == '4':
            while True:
                menu_gestion_autores()
                opcion_autor = input(seleccionar_opcion).strip()
                if opcion_autor == '1':
                    print('Registrar nuevo Autor (Pendiente)')
                elif opcion_autor == '2':
                    print('Modificar Autor (Pendiente)')
                elif opcion_autor == '3':
                    print('Eliminar Autor (Pendiente)')
                elif opcion_autor == '4':
                    print('Listar todos los Autores (Pendiente)')
                elif opcion_autor == '0':
                    print(volver_menu_principal)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion == '0':
            print('Saliendo...')
            break
        else:
            print(opcion_incorrecta)
except KeyboardInterrupt:
    print('\nSaliendo por interrupción del usuario...')