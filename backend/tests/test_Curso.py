import sys
sys.path.append('..')
from service.Curso_service import CursoService
from model.Curso_model import CursoModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found, GET_NOT_FOUND_MSG

def test_find_success():
    table = FakeTable(CursoModel)
    record = table.default_values()
    table.insert(record)
    service = CursoService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = CursoService(FakeTable(CursoModel))
    message = service.find(None, PK_DEFAULT_VALUE)[0]
    assert message == GET_NOT_FOUND_MSG

def test_insert_success():
    table = FakeTable(CursoModel)
    service = CursoService(table)
    record = table.default_values()
    status_code = service.insert(record)[1]
    assert status_code == 201

def test_insert_failure():
    service = CursoService(FakeTable(CursoModel))
    status_code = service.insert({})[1]
    assert status_code == 400
