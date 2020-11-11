from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


PK_DEFAULT_VALUE = "000"

class ProfessorModel(Schema):
    RF = Str(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    nome = Str()
    especialidade = Str()
    foto = Str()


