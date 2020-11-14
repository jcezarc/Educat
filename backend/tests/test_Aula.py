import sys
sys.path.append('..')
from service.Aula_service import AulaService
from model.Aula_model import AulaModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found

def test_find_success():
    table = FakeTable(AulaModel)
    record = table.default_values()
    table.insert(record)
    service = AulaService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = AulaService(FakeTable(AulaModel))
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 404

def test_update_success():
    table = FakeTable(AulaModel)
    service = AulaService(table)
    record = table.default_values()
    status_code = service.update(record)[1]
    assert status_code == 200

def test_update_failure():
    service = AulaService(FakeTable(AulaModel))
    status_code = service.update({})[1]
    assert status_code == 400
