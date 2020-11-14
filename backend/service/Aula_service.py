import logging
from datetime import datetime
from model.Aula_model import AulaModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class AulaService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(AulaModel)

    def find(self, params, id=None):
        logging.info('Buscando aula de hoje...')
        found = self.table.find_all(
            20,
            self.table.get_conditions({
                'dia': datetime.today().strftime('%Y-%m-%d')
            }, False)
        )
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def update(self, json):
        logging.info('Alterando lista de presença da Aula ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Registro alterado OK!")
