import uuid
import random
from faker import Faker
from datetime import datetime

def set_name_foto(record, fake):
    name = fake.name()
    record['nome'] = name
    record['foto'] = '{}{}.png'.format(
        fake.url(), name.replace(' ','')
    )

def fake_aluno(fake):
    a = {}
    a['id'] = str(uuid.uuid4())
    a['RA'] = fake.credit_card_number()
    set_name_foto(a, fake)
    return a

def fake_professor(fake):
    p = {}
    p['id'] = str(uuid.uuid4())
    p['RF'] = fake.credit_card_number()
    set_name_foto(p, fake)
    count = random.randint(2, 7)
    especs = [fake.job() for _ in range(count)]
    p['especialidade'] = especs
    return p

def fake_curso(fake):
    professor = fake_professor(fake)
    level = random.randint(1, 3)
    especs = professor['especialidade']
    c = {}
    c['id'] = str(uuid.uuid4())
    c['nome'] = '{} {}'.format(
        random.choice(especs), level
    )
    c['sala'] = '{}{}'.format(
        random.randint(1, 12),
        random.choice(['A', 'B', 'C', 'D'])
    )
    professor['especialidade'] = ','.join(especs)
    c['professor'] = professor
    return c

def fake_aula(count=10):
    fake = Faker('pt_BR')
    curso = fake_curso(fake)
    lista = []
    today = datetime.today().strftime('%Y-%m-%d')
    while len(lista) < count:
        u = {}
        u['dia'] = today
        u['curso'] = curso['id']
        u['aluno'] = fake_aluno(fake)
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
