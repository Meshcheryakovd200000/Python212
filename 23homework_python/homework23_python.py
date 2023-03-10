class Sphere:
    pi = 3.14159265359

    def __init__(self, x, y, z, r):
        self.x_None = x
        self.y_None = y
        self.z_None = z
        self.r_None = r

    def get_volume(self):
        return 4 / 3 * Sphere.pi * self.r_None ** 3

    def get_square(self):
        return 4 * Sphere.pi * self.r_None ** 2

    def get_radius(self):
        return self.r_None

    def set_radius(self, r):
        self.r_None = r

    def get_center(self):
        return self.x_None, self.y_None, self.z_None

    def set_center(self, x, y, z):
        self.x_None, self.y_None, self.z_None = x, y, z

    def is_point_inside(self, x, y, z):  # нахождение точки внутри сферы
        if ((self.x_None - x) ** 2 + (self.y_None - y) ** 2 + (self.z_None - z) ** 2) <= self.r_None ** 2:
            return True
        else:
            return False


sphere = Sphere(0, 0, 0, 0.6)

print(f"get_radius: {sphere.get_radius()}")
print(f"get_volume: {sphere.get_volume()}")
print(f"get_square: {sphere.get_square()}")
print(f"get_center: {sphere.get_center()}")
print("is_point_inside(0, -1.5, 0):", sphere.is_point_inside(0, -1.5, 0))
sphere.set_radius(1.6)
print("set_radius(1.6):", sphere.get_radius())
print("is_point_inside(0, -1.5, 0):", sphere.is_point_inside(0, -1.5, 0))
