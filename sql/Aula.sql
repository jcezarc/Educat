CREATE TABLE Aula(
    id INT,
    dia DATE ,
    aluno INT,
    curso INT,
    presente BOOLEAN,
    FOREIGN KEY (aluno) REFERENCES Aluno(id),
    FOREIGN KEY (curso) REFERENCES Curso(id),
    PRIMARY KEY(id)
);