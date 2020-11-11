import logging
from model.Aluno_model import AlunoModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class AlunoService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(AlunoModel)

    def find(self, params, RA=None):
        if RA is None:
            logging.info('Finding all records of Aluno...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        else:
            logging.info(f'Finding "{RA}" in Aluno ...')
            found = self.table.find_one([RA])
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('New record write in Aluno')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Changing record of Aluno ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Record changed OK!")
        
    def delete(self, RA):
        logging.info('Removing record of Aluno ...')
        self.table.delete(RA)
        return resp_ok("Deleted record OK!")
