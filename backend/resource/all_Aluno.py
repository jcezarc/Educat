import json
from flask_restful import Resource
from flask import request, jsonify

from service.Aluno_service import AlunoService

class AllAluno(Resource):

    
    def get(self):
        """
        Returns all records from the table Aluno

        #Read
        """
        service = AlunoService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Write a new record in Aluno

        #Write
        """
        req_data = request.get_json()
        service = AlunoService()
        return service.insert(req_data)

    
    def put(self):
        """
        Updates a record in Aluno

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = AlunoService()
        return service.update(req_data)
