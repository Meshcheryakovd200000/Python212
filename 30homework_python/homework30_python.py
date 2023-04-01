class Integer:  # Дескрипторы
    @staticmethod
    def verify_coord(coord):
        if not isinstance(coord, int):
            raise TypeError(f"Координата {coord} должна быть целым числом")
        if coord < 0:
            raise ValueError(f'Значение {coord} должно быть положительным.')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Triangle:
    side1 = Integer()
    side2 = Integer()
    side3 = Integer()

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def existence_triangle(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 \
                and self.side2 + self.side3 > self.side1:
            print(f"Треугольник cо сторанами {self.side1, self.side2, self.side3} существует.")
        else:
            print(f"Треугольник cо сторанами {self.side1, self.side2, self.side3} не существует.")


s1 = Triangle(2, 5, 6)
s2 = Triangle(5, 2, 8)
s3 = Triangle(7, 3, 6)
# print(s1.side1)
# print(s1.__dict__)
s1.existence_triangle()
s2.existence_triangle()
s3.existence_triangle()
