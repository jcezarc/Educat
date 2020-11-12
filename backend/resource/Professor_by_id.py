from flask_restful import Resource


from service.Professor_service import ProfessorService

class ProfessorById(Resource):

    

    
    def get(self, id):
        """
        Search in  Professor by the field id

        #Read
        """
        service = ProfessorService()
        return service.find(None, id)

    
    def delete(self, id):
        """
        Delete a record of Professor

        #Write
        """
        service = ProfessorService()
        return service.delete([id])
