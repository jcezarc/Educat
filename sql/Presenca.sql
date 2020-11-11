CREATE TABLE Presenca(
    id INT PRIMARY KEY,
    dia DATE ,
    situacao VARCHAR(100) ,

    FOREIGN KEY (aluno) REFERENCES Aluno,
    FOREIGN KEY (aula) REFERENCES Aula,

)