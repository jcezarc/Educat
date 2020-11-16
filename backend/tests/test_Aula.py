import sys
sys.path.append('..')
from service.Aula_service import AulaService
from model.Aula_model import AulaModel, PK_DEFAULT_VALUE
from util.db.lite_table import LiteTable
from util.messages import resp_ok, resp_not_found
from util.generator import aulas_fake

def get_service():
    table = LiteTable(
        AulaModel, {
            'database': ':memory:'
        }
    )
    table.create_table()
    AulaService.first_time = False
    service = AulaService(table)
    service.start_db()
    return service

DEFAULT_SERVICE = get_service()


def test_find_success():
    service = DEFAULT_SERVICE
    # --- Consulta a aula de hoje: ---
    res, status_code = service.find()
    assert status_code == 200

def test_find_failure():
    service = DEFAULT_SERVICE
    # --- Tenta consultar uma data que não existe: ---
    status_code = service.find('2012-12-12')[1]
    assert status_code == 404

def test_update_success():
    presenca = {
        'presente': int(True)
    }
    service = DEFAULT_SERVICE
    # --- Marca presença para a 
    #    aluna Natalia Rios Faustino:
    # -------------------------------
    record = service.table.find_one({'aluno': 4})
    record.update(presenca)
    status_code = service.update(record)[1]
    # --- Sucesso no update: ------
    assert status_code == 200
    # --- Consulta alunos com presença na aula: ---
    record = service.table.find_one(presenca)
    assert record['aluno']['id'] == 4

def test_update_failure():
    service = DEFAULT_SERVICE
    # --- Tenta realizar um comando inválido: ---
    status_code = service.update({})[1]
    assert status_code == 400
