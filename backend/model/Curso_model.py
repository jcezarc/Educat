from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Professor_model import ProfessorModel


PK_DEFAULT_VALUE = 0

class CursoModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE)
    nome = Str(required=True, default='')
    sala = Str()
    horario = Str()
    foto = Str()
    professor = Nested(ProfessorModel)

