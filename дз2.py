import math

class Point:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def length(self, other):
        #print("x self", self.x, "y self", self.y, "x other", other.x, "y other", other.y)
        length = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return length




class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        perimeter = a.length(b) + b.length(c) + c.length(a)
        return perimeter

    def square(self):
        pep = (a.length(b) + b.length(c) + c.length(a))/2
        square = math.sqrt(pep * (pep - a.length(b)) * (pep - b.length(c)) * (pep - c.length(a)))
        return square


x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]
a = Point(x, y)
b = Point(x1, y1)
c = Point(x2, y2)
z = Triangle(a, b, c)
print(z.square(), z.perimeter())
