# -*- coding: utf-8 -*-
import logging
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from resource.user_controller import valid_user
from util.swagger_generator import FlaskSwaggerGenerator
from model.Aluno_model import AlunoModel
from resource.Aluno_by_id import AlunoById
from resource.all_Aluno import AllAluno
from model.Professor_model import ProfessorModel
from resource.Professor_by_id import ProfessorById
from resource.all_Professor import AllProfessor
from model.Curso_model import CursoModel
from resource.Curso_by_id import CursoById
from resource.all_Curso import AllCurso
from model.Aula_model import AulaModel
from resource.Aula_by_id import AulaById
from resource.all_Aula import AllAula


BASE_PATH = '/educat'

def config_routes(app):
    api = Api(app)
    #--- Resources: ----
    api.add_resource(AlunoById, f'{BASE_PATH}/Aluno/<id>', methods=['GET'], endpoint='get_Aluno_by_id')
    api.add_resource(AllAluno, f'{BASE_PATH}/Aluno', methods=['GET'], endpoint='get_AllAluno')
    api.add_resource(AllAluno, f'{BASE_PATH}/Aluno', methods=['POST'], endpoint='post_Aluno')
    api.add_resource(AllAluno, f'{BASE_PATH}/Aluno', methods=['PUT'], endpoint='put_Aluno')
    api.add_resource(AlunoById, f'{BASE_PATH}/Aluno/<id>', methods=['DELETE'], endpoint='delete_Aluno')
    api.add_resource(ProfessorById, f'{BASE_PATH}/Professor/<id>', methods=['GET'], endpoint='get_Professor_by_id')
    api.add_resource(AllProfessor, f'{BASE_PATH}/Professor', methods=['GET'], endpoint='get_AllProfessor')
    api.add_resource(AllProfessor, f'{BASE_PATH}/Professor', methods=['POST'], endpoint='post_Professor')
    api.add_resource(AllProfessor, f'{BASE_PATH}/Professor', methods=['PUT'], endpoint='put_Professor')
    api.add_resource(ProfessorById, f'{BASE_PATH}/Professor/<id>', methods=['DELETE'], endpoint='delete_Professor')
    api.add_resource(CursoById, f'{BASE_PATH}/Curso/<id>', methods=['GET'], endpoint='get_Curso_by_id')
    api.add_resource(AllCurso, f'{BASE_PATH}/Curso', methods=['GET'], endpoint='get_AllCurso')
    api.add_resource(AllCurso, f'{BASE_PATH}/Curso', methods=['POST'], endpoint='post_Curso')
    api.add_resource(AllCurso, f'{BASE_PATH}/Curso', methods=['PUT'], endpoint='put_Curso')
    api.add_resource(CursoById, f'{BASE_PATH}/Curso/<id>', methods=['DELETE'], endpoint='delete_Curso')
    api.add_resource(AulaById, f'{BASE_PATH}/Aula/<id>', methods=['GET'], endpoint='get_Aula_by_id')
    api.add_resource(AllAula, f'{BASE_PATH}/Aula', methods=['GET'], endpoint='get_AllAula')
    api.add_resource(AllAula, f'{BASE_PATH}/Aula', methods=['POST'], endpoint='post_Aula')
    api.add_resource(AllAula, f'{BASE_PATH}/Aula', methods=['PUT'], endpoint='put_Aula')
    api.add_resource(AulaById, f'{BASE_PATH}/Aula/<id>', methods=['DELETE'], endpoint='delete_Aula')
    
    #-------------------

def set_swagger(app):
    swagger_url = '/docs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/api',
        config={
            'app_name': "*- educat -*"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


def swagger_details(args):
    id_route = args[0]
    params = args[1]
    model = None
    resource = None
    docstring = ""
    if id_route == 'docs':
        docstring = """Swagger documentation
        #Doc
        """
    elif id_route == 'Aluno':
        if not params:
            resource = AllAluno
        else:
            resource = AlunoById
        model = AlunoModel()
    elif id_route == 'Professor':
        if not params:
            resource = AllProfessor
        else:
            resource = ProfessorById
        model = ProfessorModel()
    elif id_route == 'Curso':
        if not params:
            resource = AllCurso
        else:
            resource = CursoById
        model = CursoModel()
    elif id_route == 'Aula':
        if not params:
            resource = AllAula
        else:
            resource = AulaById
        model = AulaModel()
    
    ignore = False
    return model, resource, docstring, ignore

logging.basicConfig(
    filename='educat.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

APP = Flask(__name__)
CORS(APP)

config_routes(APP)
set_swagger(APP)

@APP.route('/api')
def get_api():
    """
    API json data

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)

@APP.route('/health')
def health():
    return 'OK', 200



if __name__ == '__main__':
    APP.run(debug=True)
