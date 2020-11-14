# -*- coding: utf-8 -*-
import logging
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from util.swagger_generator import FlaskSwaggerGenerator
from model.Aula_model import AulaModel
from resource.all_Aula import AllAula


BASE_PATH = '/educat'

def config_routes(app):
    api = Api(app)
    #--- Resources: ----   
    api.add_resource(AllAula, f'{BASE_PATH}/Aula', methods=['GET'], endpoint='get_AllAula')
    api.add_resource(AllAula, f'{BASE_PATH}/Aula', methods=['PUT'], endpoint='put_Aula')
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
        docstring = """Documentação Swagger
        #Doc
        """
    elif id_route == 'Aula':
        resource = AllAula
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
    Dados JSON  para API de documentação

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)



if __name__ == '__main__':
    APP.run(debug=True)
