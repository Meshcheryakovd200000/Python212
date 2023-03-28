# video Python, 16.02.2023, 43 пара main22
import os.path
import time


# ----------------------------------------------------------------------
# Задача: Написать программу, осуществляющую проверку, существует ли указанный файл. Если файл существует, выведите на
# экран имя этого файла и имя его директории, а также время последнего доступа к файлу. Если файл не существует,
# выведите соответствующее сообщение.
# file_path = r'D:\Python212\Python\work_python\22python\test.txt'
# # file_path = r'test.txt'
#
# if os.path.exists(file_path):  # проверка на существование файла метод exists()
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getmtime(file_path)
#     print(f"{name} ({dirs}) - last access time {time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime))}")  # время
#     # последнего доступа к файлу
# else:
#     print(f"File {file_path} does not exist!")  # если файл не существует
#
#
# print(os.path.isfile(file_path))  # возвращает True, если указанный путь является файлом
# print(os.path.isdir(file_path))  # возвращает True, если указанный путь является директорией

# video 14 minut

# Задача:Написать программу, которая просканирует выбранную директорию и для всех её объектов выведет следующуюинформацию на экран: имя – тип – размер (только для файлов)
# •	Типы объектов: файл, директория
# •	Размер: только для файлов

# dir_name = r'D:\Python212\Python\work_python\22python'
#
# obj = os.listdir(dir_name)
# print(obj)
#
# for i in obj:
#     p = os.path.join(dir_name, i)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{i} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{i} - dir')


# -------------------------------------------------------------------------------------------------------------------
# ООП (объектно-ориентированное программирование)
# (video 43пара 28минута) начало введение в ООП)
# --------------------------------------------------------------------------------------------------------------------

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# print(dir(Point))
# print(Point.__doc__)

# class Point3D:
#     pass
#
#
# #
# #
# class Point:
#     x = 1
#     y = 1  # 100
#
#
# p1 = Point()
# # p1.x = 410
# # p1.y = 200
# # Point.y = 100
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# # print(Point.__dict__)
# print(type(p1))
# print(isinstance(p1, Point3D))
#
# # p2 = Point()
# # print(p2.x, p2.y)
# #
# # print(id(Point))
# # print(id(p1))
# # print(id(p2))

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
#
# p1.set_coord(5, 10)
# Point.set_coord(p1, 8, 12)  # {'x': 5, 'y': 10} почти то же самое что def set_coord(self), self - экземпляр класса
# # print(p1.__dict__)
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 30
# p2.set_coord(20, 30)
# print(p2.__dict__)

# ------------------------------------

# Задача: Реализуйте класс «Человек». Необходимо хранить в полях класса: имя, дату рождения, контактный телефон,
# страну, город, домашний адрес. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = '00-00-00'
#     country = "country"
#     city = "city"
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#         self.country = country
#         self.address = address
#
#     def set_name(self, name):  # заменить Имя
#         self.name = name
#
#     def get_name(self):  # посмотреть Имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Анна")
# h1.print_info()
# print(h1.get_name())


# --------------------------------------------------------------------------------------------------------------
# Задача: Реализовать класс Автомобиль

# class Car:
#     model = "None"
#     year_of_issue = "None"
#     Manufacturer = "None"
#     Power = "None"
#     Color = "None"
#     price = "None"
#
#     def print_info(self):
#         print("Данные автомобиля".center(40, "*"))
#         print(f"Название модели:{self.model}\nГод выпуска:{self.year_of_issue}\n"
#               f"Производитель:{self.Manufacturer}\nМощность двигателя:{self.Power}\n"
#               f"Цвет машины:{self.Color}\nЦена:{self.price}")
#         print("=" * 40)
#
#     def input_info(self, model_i, year_of_issue_i, manufacturer_i, power_i, color_i, price_i):
#         self.model = model_i
#         self.year_of_issue = year_of_issue_i
#         self.Manufacturer = manufacturer_i
#         self.Power = power_i
#         self.Color = color_i
#         self.price = price_i
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, value):
#         self.model = value
#
#
# h1 = Car()
# h1.print_info()
# h1.input_info("X7 M501", "2021", "BMW", "530 л.с.", "white", "10790000")
# h1.print_info()
# h1.set_model('Y7')
# print(h1.get_model())
# h1.print_info()

# ---------------------------------------------------------------------------
# Задача: Создать класс Person с данными о сотруднике (имя, фамилия) и двумя методами. Первый должен выводить данные
# о сотруднике, второй должен увеличивать квалификации сотрудника на передаваемое количество единиц.


# class Person:
#     skill = 10
#
#     # name = ""
#     # surname = ""
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Инициализатор {self.name} {self.surname}")
#
#     def __del__(self):
#         print("Удаление экземпляра\n\n")
#
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.name}", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)

# Задача: Посчитать кол-во экземпляров класса

# class Point:
#     count = 0  # 3 , статическая переменная
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# print("count =", Point.count)
# p2 = Point(15, 20)
# print(p2.count)
# print("count =", Point.count)
# p3 = Point(23, 39)
# print(p3.count)
# print("count =", Point.count)
# print(p1.count)


# Video 44 пара main22, 01 час 3 minuts
# Задача: Необходимо создать класс Robot. Каждый экземпляр робота нужно инициализировать. Робот должен поздороваться
# и представиться. При этом должен вестись подсчет роботов. По завершению работы роботов нужно выключить.

class Robot:
    k = 0

    def __init__(self, name):
        self.name = name
        print(f"Инициализация {self.name}")
        Robot.k += 1

    def __del__(self):
        print(self.name, "выключается!")
        Robot.k -= 1
        if Robot.k == 0:
            print(self.name, "был последним")
        else:
            print("Работающих роботов осталось:", Robot.k)

    def say_hi(self):
        print("Приветствую! Меня зовут:", self.name)


droid1 = Robot('R2-D2')
droid1.say_hi()
#Robot.say_hi(droid1)
print("Численность роботов:", Robot.k)

droid2 = Robot('C-3PO')
droid2.say_hi()
print("Численность роботов:", Robot.k)

print()
del droid1
del droid2
print("Численность роботов:", Robot.k)
