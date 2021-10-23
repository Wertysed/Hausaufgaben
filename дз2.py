import math

class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def length(self, other):
        print("x other", other.x, "y other", other.y)
        self.length = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


class Triangle:
    def __init__(self, a, b, c):
        self.perimeter = a + b + c
        self.poluper = (a + b + c)/2
        pep = self.poluper
        self.plosh = math.sqrt(pep*(pep - a)*(pep - b)*(pep - c))


x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]
a = Point(x, y)
b = Point(x1, y1)
c = Point(x2, y2)
#a_treu = Triangle(a.length(b), b.length(c), c.length(a))
print(a.length(b))
print(b.length(c))
print(c.length(a))
#p = Point(x, y, x1, y1)
#k = p.length
#print(a_treu.perimeter, a_treu.plosh)