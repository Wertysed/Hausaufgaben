import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def length(self, other):
    #    #print("x self", self.x, "y self", self.y, "x other", other.x, "y other", other.y)
    #   length = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    #   return length


class Vector(Point):
    def __init__(self, x, y, x1, y1):
        Point.__init__(self, x, y)
        self.x1 = x1
        self.y1 = y1

    def length(self):
        # print("x self", self.x, "y self", self.y, "x other", other.x, "y other", other.y)
        length = math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)
        return length

    def sum_of_vectors(self, other):
        print("это другое", other.length())
        sum_of_vectors = self.length() + other.length()
        return sum_of_vectors

    def subtraction_of_vectors(self, other):
        subtraction_of_vectors = self.length() - other.length()
        return subtraction_of_vectors

    def multiplications_of_vector(self, number):
        multiplications_of_vector = number * self.length()
        return multiplications_of_vector

    def scalar_product(self, other, angle):
        scalar_product = self.length() * other.length() * math.cos(angle)
        return scalar_product


x, y, x1, y1, x2, y2, x3, y3, angle, number = [int(x) for x in input().split()]

p = Vector(x, y, x1, y1)
c = Vector(x2, y2, x3, y3)
print("ЭТо не то", p.length(), p.sum_of_vectors(c), p.subtraction_of_vectors(c), p.multiplications_of_vector(number), p.scalar_product(c, angle))
