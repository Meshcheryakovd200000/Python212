from faker import Faker

from models_car.database import create_db, Session
from models_car.car import Car
from models_car.group import Group


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    group1 = Group(group_name="Jeep")
    group2 = Group(group_name="einen Wagen")
    session.add(group1)
    session.add(group2)

    faker = Faker('ru_RU')
    group_list = [group1, group2]
    session.commit()  # чтобы данные записались в БД

    for _ in range(11):
        full_name = faker.company()
        age = faker.random.randint(0, 10)
        group = faker.random.choice(group_list)
        car = Car(full_name, age, group.group_name)
        session.add(car)

    session.commit()
    session.close()
