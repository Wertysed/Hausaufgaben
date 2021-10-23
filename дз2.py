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

    def __init__(self, a, b, c, f):
        self.a = a
        self.b = b
        self.c = c
        self.f = f

    def perimeter(self):
        perimeter = a.length(b) + b.length(c) + c.length(a)
        return perimeter

    def square(self):
        pep = (a.length(b) + b.length(c) + c.length(a))/2
        square = math.sqrt(pep * (pep - a.length(b)) * (pep - b.length(c)) * (pep - c.length(a)))
        return square
    def location(self):
        pep = (a.length(b) + b.length(c) + c.length(a)) / 2
        square = math.sqrt(pep * (pep - a.length(b)) * (pep - b.length(c)) * (pep - c.length(a)))
        perimeter_f = (a.length(f) + f.length(b) + b.length(a))/2
        perimeter_f1 = (b.length(f) + f.length(c) + c.length(b))/2
        perimeter_f2 = (c.length(f) + f.length(a) + a.length(c))/2
        square_f = math.sqrt(perimeter_f * (perimeter_f - a.length(f))*(perimeter_f - f.length(b))*(perimeter_f - b.length(a)))
        square_f1 = math.sqrt(perimeter_f1 * (perimeter_f1 - b.length(f)) * (perimeter_f1 - f.length(c)) * (perimeter_f1 - c.length(b)))
        square_f2 = math.sqrt(perimeter_f2 * (perimeter_f2 - c.length(f)) * (perimeter_f2 - f.length(a)) * (perimeter_f2 - a.length(c)))
        if square_f1 + square_f + square_f2 == square:
            return 'in'
        else:
            return 'out'

x, y, x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
a = Point(x, y)
b = Point(x1, y1)
c = Point(x2, y2)
f = Point(x3, y3)
z = Triangle(a, b, c, f)
print(z.square(), z.perimeter(), z.location())
