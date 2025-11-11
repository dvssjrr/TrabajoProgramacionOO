USE biblioteca_digital;

CREATE TABLE IF NOT EXISTS `autores` (
    `id` INTEGER AUTO_INCREMENT,
    `nombre` VARCHAR(100) NOT NULL,
    `apellido` VARCHAR(100) NOT NULL,
    `nacionalidad` VARCHAR(50) NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `generos` (
    `id` INTEGER AUTO_INCREMENT,
    `nombre_genero` VARCHAR(50) NOT NULL UNIQUE,
    `descripcion` VARCHAR(255) NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `libros` (
    `id` INTEGER AUTO_INCREMENT,
    `isbn` CHAR(13) NOT NULL UNIQUE,
    `titulo` VARCHAR(255) NOT NULL,
    `anio_publicacion` CHAR(4) NULL,
    `editorial` VARCHAR(100) NULL,
    `copias_disponibles` INT NOT NULL DEFAULT 0,
    `habilitado` TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `libro_autor` (
    `id_libro` INT NOT NULL,
    `id_autor` INT NOT NULL,
    PRIMARY KEY (`id_libro`, `id_autor`),
    CONSTRAINT `fk_la_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_la_autor` FOREIGN KEY (`id_autor`) REFERENCES `autores`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `libro_genero` (
    `id_libro` INT NOT NULL,
    `id_genero` INT NOT NULL,
    PRIMARY KEY (`id_libro`, `id_genero`),
    CONSTRAINT `fk_lg_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_lg_genero` FOREIGN KEY (`id_genero`) REFERENCES `generos`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `tipos_suscripcion` (
    `id` INTEGER AUTO_INCREMENT,
    `nombre_suscripcion` VARCHAR(50) NOT NULL UNIQUE,
    `limite_libros` INT NOT NULL DEFAULT 1,
    `dias_prestamo` INT NOT NULL DEFAULT 7,
    `costo_mensual` FLOAT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `clientes` (
    `id` INT AUTO_INCREMENT,
    `rut_cliente` VARCHAR(15) NULL UNIQUE,
    `nombre_completo` VARCHAR(255) NOT NULL,
    `correo_contacto` VARCHAR(255) NOT NULL UNIQUE,
    `telefono_contacto` VARCHAR(12) NULL,
    `habilitado` TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `suscripcion` (
    `id` INT AUTO_INCREMENT,
    `fecha_inicio` DATE NOT NULL,
    `fecha_fin` DATE NULL,
    `activa` TINYINT NOT NULL DEFAULT 1,
    `id_cliente` INT NOT NULL UNIQUE,
    `id_tipo_suscripcion` INT NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_susc_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_susc_tipo` FOREIGN KEY (`id_tipo_suscripcion`) REFERENCES `tipos_suscripcion`(`id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `usuario` (
    `id` INT AUTO_INCREMENT,
    `nombre_usuario` VARCHAR(50) NOT NULL UNIQUE,
    `contrasena_hash` VARCHAR(255) NOT NULL,
    `es_admin` TINYINT NOT NULL DEFAULT 0,
    `habilitado` TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `prestamos` (
    `id` INT AUTO_INCREMENT,
    `fecha_prestamo` DATETIME NOT NULL,
    `fecha_devolucion_limite` DATETIME NOT NULL,
    `fecha_devolucion_real` DATETIME NULL,
    `multa_total` FLOAT NULL DEFAULT 0,
    `devuelto` TINYINT NOT NULL DEFAULT 0,
    `id_cliente` INT NOT NULL,
    `id_libro` INT NOT NULL,
    `id_bibliotecario` INT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_pres_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_pres_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_pres_bibliotecario` FOREIGN KEY (`id_bibliotecario`) REFERENCES `usuario`(`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `descarga` (
    `id` INT AUTO_INCREMENT,
    `fecha_descarga` DATETIME NOT NULL,
    `id_cliente` INT NOT NULL,
    `id_libro` INT NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_desc_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_desc_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `reseña` (
    `id` INT AUTO_INCREMENT,
    `calificacion` INT NOT NULL,
    `comentario` TEXT NULL,
    `fecha_resena` DATETIME NOT NULL,
    `id_cliente` INT NOT NULL,
    `id_libro` INT NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_res_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_res_libro` FOREIGN KEY (`id_libro`) REFERENCES `libros`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
