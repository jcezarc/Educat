from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


PK_DEFAULT_VALUE = 0

class AlunoModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE)
    nome = Str(required=True, default='')
    foto = Str()

