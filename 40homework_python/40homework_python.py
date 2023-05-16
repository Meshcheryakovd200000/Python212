import os

from sqlalchemy import not_
from models_car.database import DATABASE_NAME, Session
import create_database as db_creator

from models_car.car import Car
from models_car.group import Group


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

session = Session()

# for name in session.query(Car):
#     print(name.name)  # выводим все компании
# print("*" * 50)

# print(session.query(Car).count())
# print("*" * 50)

# print(session.query(Car).first())
# print("*" * 50)

# for it in session.query(Car).filter(Car.id > 7):
#     print(it)
# print("*" * 50)

# for it in session.query(Car).filter(Car.id >= 3, Car.name.like('ООО%')):
#     print(it)
# print("*" * 50)

# for it in session.query(Car).filter(not_(Car.id <= 5), not_(Car.name.like('Р%'))):
#     print(it)  # not_ преобразует только один элемент, поэтому not_ ставим перед каждым
# print("*" * 50)

# print(session.query(Car).filter(Car.name.notin_(['РАО «Исаев Осипова»', 'ООО «Гусев-Мясникова»'])).all())

# print(session.query(Car).filter(Car.age.between(3, 5)).all())
# print("*" * 50)  # возраст между

# print(session.query(Car).filter(Car.age.like("1%")).all())
# print("*" * 50)

# for it in session.query(Car).filter(Car.age.like("1%")):
#     print(it)  # возраст машины like("1%")
# print("*" * 50)

for it in session.query(Car).filter(Car.age.like("%")).limit(4):
    print(it)  # вывод 4-ёх первых записей
print("*" * 50)

