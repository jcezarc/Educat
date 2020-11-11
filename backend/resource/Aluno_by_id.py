from flask_restful import Resource


from service.Aluno_service import AlunoService

class AlunoById(Resource):

    

    
    def get(self, RA):
        """
        Search in  Aluno by the field RA

        #Read
        """
        service = AlunoService()
        return service.find(None, RA)

    
    def delete(self, RA):
        """
        Delete a record of Aluno

        #Write
        """
        service = AlunoService()
        return service.delete([RA])
