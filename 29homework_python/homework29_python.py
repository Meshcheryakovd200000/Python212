class Shape:
    def __init__(self, color, object_area, perimeter):
        self.color = color
        self.object_area = object_area
        self.perimeter = perimeter

    def info(self):
        print(f"{self.color} {self.object_area} {self.perimeter}")


class Square(Shape):
    def __init__(self, side, color, object_area, perimeter):
        self.side = side
        super().__init__(color, object_area, perimeter)

    def info(self):
        print(f"Сторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.object_area}\nПериметр: {self.perimeter} ")


group = [
    Square(3, "red", 9, 12)
]

for i in group:
    i.info()
