import os
import random
from faker import Faker
from datetime import datetime
from faker.providers import BaseProvider

ASSETS_FMT = 'assets/img/{}'
TODAS_SALAS = ['1A', '2B', '3C',]
HORARIOS = [
    'seg-sex: 08h-12h',
    'sab.: 13h-20h',
    'ter, qua, qui: 11h-15h'
]

class EducatProvider(BaseProvider):
    FRONTEND_PATH = '../frontend/src/'
    source = {}
    index = 0
    def choose_or_create_record(self, type):
        data = self.source.setdefault(type, [])
        if not data:
            path = ASSETS_FMT.format(type)
            target = os.path.join(self.FRONTEND_PATH,path)
            for f in os.listdir(target):
                record = {}
                record['id'] = len(data)+1
                record['nome'] = f.replace('.png', '')
                record['foto'] = path + '/' + f
                if type == 'curso':
                    record['sala'] = random.choice(TODAS_SALAS)
                    record['horario'] = random.choice(HORARIOS)                
                data.append(record)
        if type == 'aluno':
            pos = self.index % len(data)
            self.index = pos + 1
            return data[pos]
        return random.choice(data)
    def aluno(self):
        return self.choose_or_create_record('aluno')
    def professor(self):
        return self.choose_or_create_record('professor')
    def curso(self):
        return self.choose_or_create_record('curso')


def aulas_fake(last_id, test_mode=False, count=5):
    fake = Faker('pt_BR')
    if test_mode:
        EducatProvider.FRONTEND_PATH = '../../frontend/src/'
    fake.add_provider(EducatProvider)
    curso = fake.curso()
    curso['professor'] = fake.professor()
    lista = []
    today = datetime.today()
    while len(lista) < count:
        last_id += 1
        lista.append({
            'dia': today.strftime('%Y-%m-%d'),
            'aluno': fake.aluno(),
            'id': last_id
        })
    return {
        'curso': curso,
        'lista': lista,
    }

def run_generator_tests(dados=None):
    EducatProvider.index['curso'] = 2
    EducatProvider.index['professor'] = 1
    def exibe_dados(curso, lista):
        print('='*100)
        print('Curso:', curso)
        for item in lista:
            print('-'*100)
            print(item)
    if dados is None:
        dados = aulas_fake(0, True)
    exibe_dados(**dados)

if __name__ == '__main__':
    run_generator_tests()
