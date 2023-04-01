from abc import abstractmethod
from math import sqrt


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def object_area(self):
        pass

    @abstractmethod
    def painting(self):
        pass

    @abstractmethod
    def info(self):
        object_area = self.object_area()
        perimeter = self.perimeter()
        print(f"Площадь: {object_area}", end="")
        print(f"\nПериметр: {perimeter}")


class Square(Shape):
    def __init__(self, side1, color):
        self.side1 = side1
        super().__init__(color)

    def perimeter(self):
        return self.side1 * 4

    def object_area(self):
        return self.side1 ** 2

    def info(self):
        print("===Квадрат===")
        object_area = self.object_area()
        perimeter = self.perimeter()
        print(f"Сторона: {self.side1}\nЦвет: {self.color}\nПлощадь: {object_area}\nПериметр: {perimeter} ")

    def painting(self):
        for j in range(self.side1):
            print("*" * self.side1)


class Rectangle(Shape):
    def __init__(self, side1, side2, color):
        self.side1 = side1
        self.side2 = side2
        super().__init__(color)

    def perimeter(self):
        return (self.side1 + self.side2) * 2

    def object_area(self):
        return self.side1 * self.side2

    def info(self):
        print("\n===Прямоугольник===")
        object_area = self.object_area()
        perimeter = self.perimeter()
        print(
            f"Длина: {self.side1}\nШирина: {self.side2}\nЦвет: {self.color}\nПлощадь: {object_area}\nПериметр: {perimeter} ")

    def painting(self):
        for j in range(self.side1):
            print("*" * self.side2)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(color)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def object_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        # print(p)
        return round(sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def info(self):
        print("\n===Треугольник===")
        object_area = self.object_area()
        perimeter = self.perimeter()
        print(
            f"Сторона1: {self.side1}\nСторона2: {self.side2}\nСторона3: {self.side3}\nЦвет: {self.color}\nПлощадь: {object_area}\nПериметр: {perimeter} ")

    # def painting(self):
    #     for j in range(1, self.side2 * 2, 2):
    #         print(('*' * j).center(self.side2 * 2))
    def painting(self):
        rows = []
        for n in range(self.side2):
            rows.append(" " * n + "*" * (self.side1 - 2 * n))
        print("\n".join(reversed(rows)))


group = [
    Square(3, "red"),
    Rectangle(3, 7, "green"),
    Triangle(11, 6, 6, "yellow")
]

for i in group:
    i.info()
    i.painting()
