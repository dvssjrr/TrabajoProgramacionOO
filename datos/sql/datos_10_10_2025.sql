USE biblioteca_digital;

INSERT IGNORE INTO autores (nombre, apellido, nacionalidad) VALUES
('Gabriel', 'García Márquez', 'Colombiana'),
('Isabel', 'Allende', 'Chilena'),
('J. R. R.', 'Tolkien', 'Británica');

INSERT IGNORE INTO generos (nombre_genero, descripcion) VALUES
('Ficción', 'Obras de ficción en general'),
('Fantasia', 'Obras de fantasía y mundos imaginarios'),
('Historia', 'Obras históricas o basadas en hechos reales');

INSERT IGNORE INTO tipos_suscripcion (nombre_suscripcion, limite_libros, dias_prestamo, costo_mensual) VALUES
('Básico', 1, 7, 0.00),
('Estándar', 3, 14, 4.99),
('Premium', 10, 30, 9.99);

INSERT IGNORE INTO clientes (rut_cliente, nombre_completo, correo_contacto, telefono_contacto, habilitado) VALUES
('12.345.678-9', 'Juan Perez', 'juan.perez@example.com', '912345678', 1),
('98.765.432-1', 'Maria Lopez', 'maria.lopez@example.com', '987654321', 1);

INSERT IGNORE INTO usuario (nombre_usuario, contrasena_hash, es_admin, habilitado) VALUES
('admin', 'hash_de_ejemplo', 1, 1);

INSERT IGNORE INTO libros (isbn, titulo, anio_publicacion, editorial, copias_disponibles, habilitado) VALUES
('9780307474278', 'Cien años de soledad', '1967', 'Sudamericana', 3, 1),
('9789563451234', 'La casa de los espiritus', '1982', 'Plaza & Janes', 2, 1),
('9780261103573', 'El señor de los anillos', '1954', 'Allen & Unwin', 5, 1);

INSERT IGNORE INTO libro_autor (id_libro, id_autor)
VALUES
((SELECT id FROM libros WHERE isbn='9780307474278'), (SELECT id FROM autores WHERE nombre='Gabriel' AND apellido='García Márquez')),
((SELECT id FROM libros WHERE isbn='9789563451234'), (SELECT id FROM autores WHERE nombre='Isabel' AND apellido='Allende')),
((SELECT id FROM libros WHERE isbn='9780261103573'), (SELECT id FROM autores WHERE nombre='J. R. R.' AND apellido='Tolkien'));

INSERT IGNORE INTO libro_genero (id_libro, id_genero)
VALUES
((SELECT id FROM libros WHERE isbn='9780307474278'), (SELECT id FROM generos WHERE nombre_genero='Ficción')),
((SELECT id FROM libros WHERE isbn='9789563451234'), (SELECT id FROM generos WHERE nombre_genero='Ficción')),
((SELECT id FROM libros WHERE isbn='9780261103573'), (SELECT id FROM generos WHERE nombre_genero='Fantasia'));
