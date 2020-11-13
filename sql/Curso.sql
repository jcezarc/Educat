CREATE TABLE Curso(
    id VARCHAR(40),
    nome VARCHAR(100) ,
    sala VARCHAR(20) ,
    horario VARCHAR(100) ,
    logotipo VARCHAR(100) ,
    professor INT,
    FOREIGN KEY (professor) REFERENCES Professor(id),
    PRIMARY KEY(id)
)