from flask_restful import Resource


from service.Aluno_service import AlunoService

class AlunoById(Resource):

    

    
    def get(self, id):
        """
        Search in  Aluno by the field id

        #Read
        """
        service = AlunoService()
        return service.find(None, id)

    
    def delete(self, id):
        """
        Delete a record of Aluno

        #Write
        """
        service = AlunoService()
        return service.delete([id])
