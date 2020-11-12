CREATE TABLE Aula(
    id INT AUTO_INCREMENT,
    dia DATE ,
    aluno INT,
    curso INT,
    FOREIGN KEY (aluno) REFERENCES Aluno(id),
    FOREIGN KEY (curso) REFERENCES Curso(id),
    PRIMARY KEY(id)
)