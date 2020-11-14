import json
from flask_restful import Resource
from flask import request, jsonify
from service.Aula_service import AulaService

class AllAula(Resource):
    
    def get(self):
        """
        Retorna todos os alunos inscritos na Aula atual

        #Consulta
        """
        service = AulaService()
        return service.find()
    
    
    def put(self):
        """
        Atualiza a lista de presença da Aula

        #Gravação
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = AulaService()
        return service.update(req_data)
