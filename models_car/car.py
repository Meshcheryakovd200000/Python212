from sqlalchemy import Column, ForeignKey, Integer, String

from models_car.database import Base


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name, age, id_group):
        self.name = full_name
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Компания покупающая автомобиль (company: {self.name}, "\
                f"Возраст машины: {self.age}, ID группы: {self.group})"
