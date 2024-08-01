import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        email=faker_ru.email(),
        salary=random.randint(20000, 800000),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile_number=faker_ru.msisdn(),
    )


def generated_file():
    path = f'/Users/qamacos/PycharmProjects/qaa_demoqa_course/filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path
