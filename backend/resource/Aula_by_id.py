from flask_restful import Resource


from service.Aula_service import AulaService

class AulaById(Resource):

    

    
    def get(self, id):
        """
        Search in  Aula by the field id

        #Read
        """
        service = AulaService()
        return service.find(None, id)

    
    def delete(self, id):
        """
        Delete a record of Aula

        #Write
        """
        service = AulaService()
        return service.delete([id])
