import logging
from model.Professor_model import ProfessorModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class ProfessorService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(ProfessorModel)

    def find(self, params, RF=None):
        if RF is None:
            logging.info('Finding all records of Professor...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        else:
            logging.info(f'Finding "{RF}" in Professor ...')
            found = self.table.find_one([RF])
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('New record write in Professor')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Changing record of Professor ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Record changed OK!")
        
    def delete(self, RF):
        logging.info('Removing record of Professor ...')
        self.table.delete(RF)
        return resp_ok("Deleted record OK!")
