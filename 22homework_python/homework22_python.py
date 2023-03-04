from math import sqrt


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        print(f"Длина прямоугольника: {self.length}")
        self.width = width
        print(f"Ширина прямоугольника: {self.width}")

    def square(self):
        square = self.length * self.width
        print(f"Площадь прямоугольника: {square}")

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"Периметр прямоугольника: {perimeter}")

    def hypotenuse(self):
        hypotenuse = round(sqrt(self.length ** 2 + self.width ** 2), 2)
        print(f"Гипотенуза прямоугольника: {hypotenuse}")

    def drawing(self):
        for i in range(self.length):
            print("*" * self.width)


p = Rectangle(3, 9)
p.square()
p.perimeter()
p.hypotenuse()
p.drawing()
