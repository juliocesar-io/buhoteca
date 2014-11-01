-- Created by Vertabelo (http://vertabelo.com)
-- Script type: create
-- Scope: [tables, references, sequences, views, procedures]
-- Generated at Sat Nov 01 04:06:01 UTC 2014




-- tables
-- Table: autor
CREATE TABLE autor (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    nacionalidad varchar(50)  NOT NULL,
    CONSTRAINT autor_pk PRIMARY KEY (id)
);



-- Table: libro
CREATE TABLE libro (
    id int  NOT NULL,
    titulo varchar(30)  NOT NULL,
    editorial varchar(30)  NOT NULL,
    area varchar(30)  NOT NULL,
    cover_url varchar(120)  NULL,
    digital_url varchar(120)  NULL,
    disponible_fisico boolean  NOT NULL,
    CONSTRAINT libro_pk PRIMARY KEY (id)
);



-- Table: libro_autor
CREATE TABLE libro_autor (
    id int  NOT NULL,
    Libro_id int  NOT NULL,
    Autor_id int  NOT NULL,
    CONSTRAINT libro_autor_pk PRIMARY KEY (id)
);



-- Table: prestamo
CREATE TABLE prestamo (
    id int  NOT NULL,
    fecha_prestamo date  NOT NULL,
    fecha_devolucion date  NOT NULL,
    devuelto boolean  NOT NULL,
    Usuario_id int  NOT NULL,
    Libro_id int  NOT NULL,
    CONSTRAINT prestamo_pk PRIMARY KEY (id)
);



-- Table: usuario
CREATE TABLE usuario (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    programa varchar(50)  NOT NULL,
    fecha_nacimiento date  NOT NULL,
    correo varchar(50)  NOT NULL,
    password varchar(50)  NOT NULL,
    CONSTRAINT usuario_pk PRIMARY KEY (id)
);







-- foreign keys
-- Reference:  Prestamo_Libro (table: prestamo)


ALTER TABLE prestamo ADD CONSTRAINT Prestamo_Libro 
    FOREIGN KEY (Libro_id)
    REFERENCES libro (id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE 
;

-- Reference:  Prestamo_Usuario (table: prestamo)


ALTER TABLE prestamo ADD CONSTRAINT Prestamo_Usuario 
    FOREIGN KEY (Usuario_id)
    REFERENCES usuario (id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE 
;

-- Reference:  Table_7_Autor (table: libro_autor)


ALTER TABLE libro_autor ADD CONSTRAINT Table_7_Autor 
    FOREIGN KEY (Autor_id)
    REFERENCES autor (id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE 
;

-- Reference:  Table_7_Libro (table: libro_autor)


ALTER TABLE libro_autor ADD CONSTRAINT Table_7_Libro 
    FOREIGN KEY (Libro_id)
    REFERENCES libro (id)
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE 
;






-- End of file.

