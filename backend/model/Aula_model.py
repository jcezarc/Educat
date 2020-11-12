from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Aluno_model import AlunoModel
from model.Curso_model import CursoModel


PK_DEFAULT_VALUE = 0

class AulaModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    dia = Date()

    aluno = Nested(AlunoModel)
    curso = Nested(CursoModel)

