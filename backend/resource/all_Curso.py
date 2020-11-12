import json
from flask_restful import Resource
from flask import request, jsonify

from service.Curso_service import CursoService

class AllCurso(Resource):

    
    def get(self):
        """
        Returns all records from the table Curso

        #Read
        """
        service = CursoService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Write a new record in Curso

        #Write
        """
        req_data = request.get_json()
        service = CursoService()
        return service.insert(req_data)

    
    def put(self):
        """
        Updates a record in Curso

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = CursoService()
        return service.update(req_data)
