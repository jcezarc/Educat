from flask_restful import Resource


from service.Presenca_service import PresencaService

class PresencaById(Resource):

    

    
    def get(self, id):
        """
        Search in  Presenca by the field id

        #Read
        """
        service = PresencaService()
        return service.find(None, id)

    
    def delete(self, id):
        """
        Delete a record of Presenca

        #Write
        """
        service = PresencaService()
        return service.delete([id])
