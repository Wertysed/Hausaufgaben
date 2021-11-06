import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def length(self, other):
    #    #print("x self", self.x, "y self", self.y, "x other", other.x, "y other", other.y)
    #   length = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    #   return length
    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def __repr__(self):
        return str(self)


class Vector(Point):
    def length(self):
        return super().distance(Point(0, 0))

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)

    # def scalar_product(self, other, angle):
    #    scalar_product = self.length() * other.length() * math.cos(angle)
    #   return scalar_product
    def __repr__(self):
        return f'Vector x={self.x}, y={self.y}'


x, y, x1, y1, number = [int(x) for x in input().split()]
if __name__ == '__main__':
    first_vector = Vector(x, y)
    second_vector = Vector(x1, y1)
    print(first_vector.length(), second_vector.length())
    print('плюс = ', first_vector + second_vector, 'минус = ', first_vector - second_vector, 'умножение = ',
          first_vector * number, second_vector * number)
