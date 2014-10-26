
-- Scripts para generar las tablas para el proyecto de la biblioteca.
-- Julio Cesar 2014


-- Tabla: Autor
CREATE TABLE Autor (
    id int  NOT NULL,
    nacionalidad varchar(50)  NOT NULL,
    CONSTRAINT Autor_pk PRIMARY KEY (id)
);



-- Tabla: Libro
CREATE TABLE Libro (
    id int  NOT NULL,
    titulo varchar(30)  NOT NULL,
    editorial varchar(30)  NOT NULL,
    area varchar(30)  NOT NULL,
    cover_url varchar(120)  NULL,
    digital_url varchar(120)  NULL,
    disponible_fisico boolean  NOT NULL,
    Autor_id int  NOT NULL,
    CONSTRAINT Libro_pk PRIMARY KEY (id)
);



-- Tabla: Prestamo
CREATE TABLE Prestamo (
    id int  NOT NULL,
    fecha_prestamo date  NOT NULL,
    fecha_devolucion date  NOT NULL,
    devuelto boolean  NOT NULL,
    Usuario_id int  NOT NULL,
    Libro_id int  NOT NULL,
    CONSTRAINT Prestamo_pk PRIMARY KEY (id)
);



-- Tabla: Usuario
CREATE TABLE Usuario (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    programa varchar(50)  NOT NULL,
    fecha_nacimiento date  NOT NULL,
    correo varchar(50)  NOT NULL,
    password varchar(50)  NOT NULL,
    CONSTRAINT Usuario_pk PRIMARY KEY (id)
);


