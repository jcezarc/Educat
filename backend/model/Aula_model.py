from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Professor_model import ProfessorModel


PK_DEFAULT_VALUE = 0

class AulaModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    descricao = Str()
    sala = Str()
    horario = Str()
    logotipo = Str()

    professor = Nested(ProfessorModel)

