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
from util.generator import aulas_fake, run_tests

class AulaService:
    first_time = True

    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(AulaModel)
        if self.first_time:
            self.first_time = False
            if self.find()[1] == 404:
                self.start_db()

    def find(self):
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

    def start_db(self):
        run_tests()
        curso, aulas = aulas_fake()
        tc = self.table.joins['curso']
        errors = tc.insert(curso)
        if errors:
            raise Exception(errors)
        curso = tc.find_one(curso)['id']
        for aula in aulas:
            aula['curso'] = curso
            self.table.insert(aula)
