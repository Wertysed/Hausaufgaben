import math


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def length(self, other):
        length = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return length

x = Point(3, 5)
b = Point(4, 7)
print(x.length(b))