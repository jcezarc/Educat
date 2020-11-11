import json
from flask_restful import Resource
from flask import request, jsonify

from service.Presenca_service import PresencaService

class AllPresenca(Resource):

    
    def get(self):
        """
        Returns all records from the table Presenca

        #Read
        """
        service = PresencaService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Write a new record in Presenca

        #Write
        """
        req_data = request.get_json()
        service = PresencaService()
        return service.insert(req_data)

    
    def put(self):
        """
        Updates a record in Presenca

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = PresencaService()
        return service.update(req_data)
