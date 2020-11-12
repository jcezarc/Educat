import logging
from model.Curso_model import CursoModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class CursoService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(CursoModel)

    def find(self, params, id=None):
        if id is None:
            logging.info('Finding all records of Curso...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        else:
            logging.info(f'Finding "{id}" in Curso ...')
            found = self.table.find_one([id])
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('New record write in Curso')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Changing record of Curso ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Record changed OK!")
        
    def delete(self, id):
        logging.info('Removing record of Curso ...')
        self.table.delete(id)
        return resp_ok("Deleted record OK!")
