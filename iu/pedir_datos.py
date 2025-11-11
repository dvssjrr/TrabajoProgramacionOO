# --- Funciones para solicitar datos de SUSCRIPCIÓN ---

def str_nombre_suscripcion():
    nombre = input('Ingrese nombre del tipo de suscripción: ')
    return nombre.title()

def str_limite_libros():
    limite = input('Ingrese límite de libros prestables: ')
    return limite

# --- Funciones para solicitar datos de CLIENTES ---

def datos_cliente():
    nombre = input('Ingrese nombre completo del cliente: ')
    email = input('Ingrese email: ')
    telefono = input('Ingrese teléfono de contacto: ')
    return nombre.title(), email.lower(), telefono

def str_id_cliente():
    id_cliente = input('Ingrese ID o Rut del Cliente a gestionar: ')
    return id_cliente

# --- Funciones adicionales para Libros/Autores ---

def str_id_autor():
    id_autor = input('Ingrese ID del Autor responsable: ')
    return id_autor

def str_id_libro():
    id_libro = input('Ingrese ID o ISBN del Libro a gestionar: ')
    return id_libro