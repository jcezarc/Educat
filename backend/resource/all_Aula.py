import json
from flask_restful import Resource
from flask import request, jsonify

from service.Aula_service import AulaService

class AllAula(Resource):

    
    def get(self):
        """
        Returns all records from the table Aula

        #Read
        """
        service = AulaService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Write a new record in Aula

        #Write
        """
        req_data = request.get_json()
        service = AulaService()
        return service.insert(req_data)

    
    def put(self):
        """
        Updates a record in Aula

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = AulaService()
        return service.update(req_data)
