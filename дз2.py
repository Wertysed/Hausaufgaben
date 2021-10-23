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


class Circle:
    def __init__(self, center,  radius):
        self.center = center
        self.radius = radius


    def length_circle(self):
        length_circle = 2 * math.pi * self.radius
        print('length')
        return length_circle

    def square_circle(self):
        square_circle = math.pi * self.radius**2
        print('sq')
        print(self.center.x)
        return square_circle
    def location_circle(self,other):
        print('loc')
        if (other.x - self.center.x)**2 + (other.y - self.center.y) < self.radius**2:
            return 'in circle'
        else:
            return 'out circle'
    def intersection(self, other):
        print('hello frov inter')
        if self.center.length(other.center) > 2 * self.radius:
            return 'out circle 2'
        else:
            return 'in circle 2'

center_x,center_y,  radius,center_x2, center_y2, radius_2, center_x1, center_y1 = [int(x) for x in input().split()]
center = Point(center_x, center_y)
center_our = Point(center_x1, center_y1)
center_2 = Point(center_x2, center_y2)
t = Circle(center, radius)
p = Circle(center_2, radius_2)
print(t.length_circle(), t.square_circle(), t.location_circle(center_our), t.intersection(p))

#t.location_circle(center_our)