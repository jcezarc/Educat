CREATE TABLE Curso(
    id INT,
    nome VARCHAR(100) ,
    sala VARCHAR(20) ,
    horario VARCHAR(100) ,
    foto VARCHAR(100) ,
    professor INT,
    FOREIGN KEY (professor) REFERENCES Professor(id),
    PRIMARY KEY(id)
);