import sys
sys.path.append('..')
from service.Presenca_service import PresencaService
from model.Presenca_model import PresencaModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found, GET_NOT_FOUND_MSG

def test_find_success():
    table = FakeTable(PresencaModel)
    record = table.default_values()
    table.insert(record)
    service = PresencaService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = PresencaService(FakeTable(PresencaModel))
    message = service.find(None, PK_DEFAULT_VALUE)[0]
    assert message == GET_NOT_FOUND_MSG

def test_insert_success():
    table = FakeTable(PresencaModel)
    service = PresencaService(table)
    record = table.default_values()
    status_code = service.insert(record)[1]
    assert status_code == 201

def test_insert_failure():
    service = PresencaService(FakeTable(PresencaModel))
    status_code = service.insert({})[1]
    assert status_code == 400
