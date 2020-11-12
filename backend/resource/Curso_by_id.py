from flask_restful import Resource


from service.Curso_service import CursoService

class CursoById(Resource):

    

    
    def get(self, id):
        """
        Search in  Curso by the field id

        #Read
        """
        service = CursoService()
        return service.find(None, id)

    
    def delete(self, id):
        """
        Delete a record of Curso

        #Write
        """
        service = CursoService()
        return service.delete([id])
