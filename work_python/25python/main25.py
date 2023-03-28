# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         # print(f)
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         # print(letters)
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 18 or old > 90:
#             raise TypeError("Возраст должен быть числом в диапазоне от 18 до 90 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, '1234 567890', 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 35
# p1.password = '4567 123456'
# p1.weight = 70.0
# print(p1.__dict__)
# --------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Наследование
# -------------------------------------------------------------------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# # print(issubclass(Point, object))  # наследуется ли класс Point от другого объекта который передаем
#

# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         print("Переопределенный инициализатор Line")
#         super().__init__(*args)  # для вызова __init__ родительского класса
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")
#
#
# # class Rect(Prop):
# #     def draw_rect(self):
# #         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # print(line.__dict__)
# # line._width = 5
# line.draw_line()
#
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()
# # print(dir(Rect))
#
#
# # DRY (Don`t Repeat Yourself) - не повторяйся!


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print("Площадь: ", end="")
#         return self.__width * self.__height
#
#     def print_info(self):
#         print(f"Прямоугольник\nШирина: {self.__width}\nВысота: {self.__height}\nЦвет: {self.color}")
#
#
# rect = Rectangle(10, 20, "зеленый")
# rect.color = "синий"
# rect.print_info()
# print(rect.area())


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            return True
        return False

    def is_int(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coord(self, sp, ep):
        print("Prop")
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")


class Line(Prop):
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def set_coord(self, sp, ep):
        print("Line")
        super().set_coord(sp, ep)
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")


class Rect(Prop):
    def draw_rect(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()
line.set_coord(Point(10, 20), Point(100, 200))
line.draw_line()
print()
rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()
rect.set_coord(Point(20.3, 30), Point(50, 70.8))
rect.draw_rect()
