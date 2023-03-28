# video 55-56 пара

# Перегрузка операторов

# Число секунд в одном дне: 24*60*60 = 86400

# class Clock:
#     __DAY = 86400  # число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __eq__(self, other):  # сравнить два элемента
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec >= other.sec
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec <= other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):  # принимаемый аргумент item если он не будет типом данных str то
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# #
# c1 = Clock(80000)
# # c1 = Clock(200)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# c1["min"] = 61
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())
# # c2 = Clock(100)
# # if c1 >= c2:
# #     print("Время Больше")
# # else:
# #     print("Время Меньше")
# #
# # c4 = Clock(300)
# #
# # c3 = c1 + c2 + c4  # c3 = Clock(300)
# # c2 += c1
# # print(c1.get_format_time())
# # print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())

# ----------------------------------------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             # return "Неверный индекс"
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5  = 6
#             self.marks.extend([None] * off)  # self.marks.extend([None] * 6) => [None, None, None, None, None, None]
#             # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value
#         # [5, 5, 3, 4, 5, None, None, None, None, None, 5]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student('Сергей', (5, 5, 3, 4, 5))
# print(s1[2])
# s1[10] = 5
# del s1[2]
# print(s1.marks)
# # print(s1.marks[2])

# --------------------------------------------
# Задача кот и кошка, рождение котят
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]  # range(0, 1) рождение котят
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# --------------------------------------------------------------------------------------------------------------------
#                                                  Полиморфизм
# --------------------------------------------------------------------------------------------------------------------

# class Rectangle:  # Прямоугольник
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:  # Квадрат
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:  # Треугольник
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# #
# for g in shape:
#     print(g.get_perimetr())
# # if isinstance(g, Rectangle):
# #     print(g.get_perimetr())
# # else:
# #     print(g.get_perimetr())
#
# # print(r1.get_perimetr(), r2.get_perimetr())
# # print(s1.get_perimetr(), s2.get_perimetr())

# -----------------------------------------------

# class Number:
#     def __init__(self, value):  # 10
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)  # 10 + 35
#
#
# class Text:
#     def __init__(self, value):  # "Python"
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  # len("Python35") = 8 символов
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))

# ---------------------------------------------------

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
# animal = [cat1, dog1]
# for i in animal:
#     print(i.info())
#     print(i.make_sound())

# ----------------------------------------------------

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# -----------------------------------------------

class Point:
    def __init__(self, *args):
        self.coord = args

    def __len__(self):
        return len(self.coord)  # колличество элементов в self.coord


p = Point(3, 1, 2)
print(len(p))

