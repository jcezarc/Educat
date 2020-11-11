from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Aluno_model import AlunoModel
from model.Aula_model import AulaModel


PK_DEFAULT_VALUE = 0

class PresencaModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    dia = Date()
    situacao = Str()

    aluno = Nested(AlunoModel)
    aula = Nested(AulaModel)

