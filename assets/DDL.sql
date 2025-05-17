CREATE TABLE supervisor
(
    id serial PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    contraseña VARCHAR(20) NOT NULL,
);

CREATE TABLE actividades
(
    id serial PRIMARY KEY,
    fecha_hora datetime NOT NULL,
    descripcion varchar(200) NOT NULL,
    condiciones_climaticas VARCHAR(100) NOT NULL,
    supervisor_id INTEGER NOT NULL,
    CONSTRAINT fk_supervisor FOREIGN KEY(supervisor_id) REFERENCES supervisor(id) MATCH SIMPLE,
    
)

CREATE TABLE anexos
(
    id serial primary key,
    id_actividad INTEGER NOT NULL,
    ruta_archivo VARCHAR(255) NOT NULL,
    tipo_archivo VARCHAR(50) NOT NULL,
    CONSTRAINT fk_actividad FOREIGN KEY(id_actividad) REFERENCES actividades(id) MATCH SIMPLE on DELETE CASCADE,

)


-- Inserta los supervisores
insert into supervisor (nombre, email, contraseña) values
("Jeronimo", "jero@gmail.com", "1234"),
("Joaquin", "joaquin@gmail.com", "5678"),
("Samuel", "samuel@hotmail.com", "91011"),
("Lucas", "lucas@yahoo.com", "1213")


-- Inserta las actividades con su supervisor correspondiente
insert into actividades (fecha_hora, descripcion, condiciones_climaticas, supervisor_id) values
("2023-10-01 10:00:00", "Actividad de prueba 1", "Soleado", 1),
("2023-10-02 11:00:00", "Actividad de prueba 2", "Nublado", 2),
("2023-10-03 12:00:00", "Actividad de prueba 3", "Lluvia", 3),
("2023-10-04 13:00:00", "Actividad de prueba 4", "Soleado", 4)


-- Inserta los anexos a las actividades correspondientes
insert into anexos (id_actividad, ruta_archivo, tipo_archivo) values
(1, "/ruta/al/archivo1.jpg", "imagen"),
(2, "/ruta/al/archivo2.pdf", "documento"),
(3, "/ruta/al/archivo3.mp4", "video"),
(4, "/ruta/al/archivo4.docx", "documento")