import os
import random
from faker import Faker
from datetime import datetime
from collections import Counter
from faker.providers import BaseProvider

FRONTEND_PATH = '../frontend/src/'
ASSETS_FMT = 'assets/img/{}'
TODAS_SALAS = ['1A', '2B', '3C',]
HORARIOS = [
    'seg-sex: 08h-12h',
    'sab.: 13h-20h',
    'ter, qua, qui: 11h-15h'
]

class EducatProvider(BaseProvider):
    source = {}
    index = Counter()
    def choose_or_create_record(self, type):
        data = self.source.setdefault(type, [])
        if not data:
            path = ASSETS_FMT.format(type)
            target = os.path.join(FRONTEND_PATH,path)
            for f in os.listdir(target):
                record = {}
                record['id'] = len(data)+1
                record['nome'] = f.replace('.png', '')
                record['foto'] = path + '/' + f
                data.append(record)
        pos = self.index[type] % len(data)
        self.index[type] = pos + 1
        return data[pos], pos
        # return random.choice(data)
    def aluno(self):
        return self.choose_or_create_record('aluno')[0]
    def professor(self):
        return self.choose_or_create_record('professor')[0]
    def curso(self):
        c, index = self.choose_or_create_record('curso')
        index %= 3
        c['sala'] = TODAS_SALAS[index]
        c['horario'] = HORARIOS[index]
        return c


def aulas_fake(count=10):
    fake = Faker('pt_BR')
    fake.add_provider(EducatProvider)
    curso = fake.curso()
    curso['professor'] = fake.professor()
    lista = []
    today = datetime.today().strftime('%Y-%m-%d')
    while len(lista) < count:
        lista.append({
            'dia': today,
            'aluno': fake.aluno(),
            'id': len(lista)+1
        })
    return {
        'curso': curso,
        'lista': lista,
    }

def run_generator_tests(dados=None):
    def exibe_dados(curso, lista):
        print('='*100)
        print('Curso:', curso)
        for item in lista:
            print('-'*100)
            print(item)
    if dados is None:
        FRONTEND_PATH = '../../frontend/src/'
        dados = aulas_fake()
    exibe_dados(**dados)

if __name__ == '__main__':
    run_generator_tests()
