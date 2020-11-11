from flask_restful import Resource


from service.Professor_service import ProfessorService

class ProfessorById(Resource):

    

    
    def get(self, RF):
        """
        Search in  Professor by the field RF

        #Read
        """
        service = ProfessorService()
        return service.find(None, RF)

    
    def delete(self, RF):
        """
        Delete a record of Professor

        #Write
        """
        service = ProfessorService()
        return service.delete([RF])
