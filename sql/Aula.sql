CREATE TABLE Aula(
    id INT PRIMARY KEY,
    descricao VARCHAR(100) ,
    sala VARCHAR(100) ,
    horario VARCHAR(100) ,
    logotipo VARCHAR(100) ,

    FOREIGN KEY (professor) REFERENCES Professor,

)