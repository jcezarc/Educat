import json
from flask_restful import Resource
from flask import request, jsonify

from service.Professor_service import ProfessorService

class AllProfessor(Resource):

    
    def get(self):
        """
        Returns all records from the table Professor

        #Read
        """
        service = ProfessorService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Write a new record in Professor

        #Write
        """
        req_data = request.get_json()
        service = ProfessorService()
        return service.insert(req_data)

    
    def put(self):
        """
        Updates a record in Professor

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = ProfessorService()
        return service.update(req_data)
