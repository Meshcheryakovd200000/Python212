import math


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_pair_a(self):
        return self.__a

    def set_pair_a(self, a_n):
        self.__a = a_n

    def get_pair_b(self):
        return self.__b

    def set_pair_b(self, b_n):
        self.__b = b_n

    p_a = property(get_pair_a, set_pair_a)
    p_b = property(get_pair_b, set_pair_b)

    def sum(self):
        return self.__a + self.__b

    def mult(self):
        return self.__a * self.__b

    def sqrt_(self):
        return self.__a ** 2 + self.__b ** 2

    def pr_info(self):
        print(f"( {self.__a}, {self.__b}", end=', ')


class RightTriangle(Pair):

    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        return print(f"Гипотенуза треугольника ABC: {round(math.sqrt(super().sqrt_()), 2)}")

    def area(self):
        return print(f"Площадь треугольника ABC: {round(super().mult() / 2, 2)}")

    def pr_info(self):
        print(f"Прямоугольный треугольник ABC ", end=' ')
        super().pr_info()
        print(f"{round(math.sqrt(super().sqrt_()), 2)} )")


r_t = RightTriangle(5, 8)
r_t.hypotenuse()
r_t.pr_info()
r_t.area()
print()
print(f"Сумма: {r_t.sum()}")
print("Произведение:", r_t.mult())
print()
r_t.p_a = 6.5
r_t.p_b = 11.04
r_t.hypotenuse()
r_t.p_a = 10
r_t.p_b = 20
r_t.hypotenuse()
print(f"Сумма: {r_t.sum()}")
print("Произведение:", r_t.mult())
r_t.area()
