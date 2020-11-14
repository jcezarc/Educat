import os
import random
from faker import Faker
from datetime import datetime
from faker.providers import BaseProvider

FRONTEND_PATH = '../../frontend/src/'
ASSETS_FMT = 'assets/img/{}'

class EducatProvider(BaseProvider):
    source = {}
    def choose_or_create_record(self, path):
        data = self.source.setdefault(path, [])
        if not data:
            path = ASSETS_FMT.format(path)
            target = os.path.join(FRONTEND_PATH,path)
            for f in os.listdir(target):
                record = {}
                record['nome'] = f.replace('.png', '')
                record['foto'] = path + '/' + f
                data.append(record)
        return random.choice(data)
    def aluno(self):
        return self.choose_or_create_record('aluno')
    def professor(self):
        return self.choose_or_create_record('professor')
    def curso(self):
        c = self.choose_or_create_record('curso')
        c['sala'] = '{}{}'.format(
            random.randint(1, 12),
            random.choice(['A', 'B', 'C', 'D'])
        )
        return c


def fake_aula(count=10):
    fake = Faker('pt_BR')
    fake.add_provider(EducatProvider)
    curso = fake.curso()
    curso['professor'] = fake.professor()
    curso['horario'] = fake.time('%H:%M')
    lista = []
    today = datetime.today().strftime('%Y-%m-%d')
    while len(lista) < count:
        u = {}
        u['dia'] = today
        u['aluno'] = fake.aluno()
        u['presente'] = False
        lista.append(u)
    return curso, lista

if __name__ == '__main__':
    curso, lista = fake_aula()
    print('='*100)
    print('Curso:', curso)
    for item in lista:
        print('-'*100)
        print(item)
