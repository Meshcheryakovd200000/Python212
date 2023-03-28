# Инкапсуляция ---------------------------------------------------------------------------------------------------
# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0  # обнуление координат
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата Y должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(1.5, 7)
# # # p1.__x = 100
# print(p1.get_coord())
# # print(p1.__x)
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# p1.set_x(8)
# p1.set_y(16)
# print(p1.get_x())
# print(p1.get_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата Y должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
#
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         print("Вызов __get")
#         return self.__x
#
#     def __set_x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("Вызов __get")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property  # getter
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = "abc"
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# del p1.name
# print(p1.__dict__)

# -------------------------

# статический метод
# video 46 para 19 minuts

# class Point:
#     __count = 0  # статическая переменная , закрытая
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1  # сколько будем создавать экземпляров класса
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(p1.__dict__)
# print(Point.get_count())
# print(p2.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# --------------------
# Задача

# class Count:
#
#     @staticmethod
#     def maxim(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def minim(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avg(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def fact(a):
#         factorial = 1
#         for i in range(1, a + 1):
#             factorial *= i
#         return factorial
#
#
# print(Count.maxim(3, 5, 7, 9))
# print(Count.minim(3, 5, 7, 9))
# print(Count.avg(3, 5, 7, 9))
# print(Count.fact(5))

import math


class Area:
    count = 0  # 5

    @staticmethod
    def triangle_area(a, b, c):
        p = (a + b + c) / 2
        Area.count += 1
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_area2(a, h):
        Area.count += 1
        return 0.5 * a * h

    @staticmethod
    def square_area(a):
        Area.count += 1
        return a ** 2

    @staticmethod
    def rect_area(a, b):
        Area.count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.count


print(f"Площадь треугольника по формуле Герона:", Area.triangle_area(3, 4, 5))
print(f"Площадь треугольника через основание и высоту:", Area.triangle_area2(6, 7))
print(f"Площадь квадрата:", Area.square_area(7))
print(f"Площадь квадрата:", Area.square_area(9))
print(f"Площадь прямоугольника:", Area.rect_area(2, 6))
print(f"Количество подсчетов площади: {Area.get_count()}")
