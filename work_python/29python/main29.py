# video 57 пара

class Human:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def info(self):
        print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")


class Student(Human):
    def __init__(self, last_name, first_name, age, speciality, group, rating):
        self.speciality = speciality
        self.group = group
        self.rating = rating
        super().__init__(last_name, first_name, age)

    def info(self):
        super().info()
        print(f"{self.speciality} {self.group} {self.rating}", end=" ")


group1 = [
    Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
    Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
    # Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    # Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
    Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
    # Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
]

for i in group1:
    i.info()
