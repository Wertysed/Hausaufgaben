from дз1Принципы import Point, Vector


class Vehicle:
    def __init__(self, start):
        self.position = start
        self.direction = Vector(0, 0)
        self.is_recording = False
        self.path = [start]

    def movement(self, time):
        for i in range(time):
            self.position = Point(self.position.x + self.direction.x, self.position.y + self.direction.y)
            if self.is_recording:
                self.path.append(self.position)


class Car(Vehicle):
    def __init__(self, start, gas, gas_per_unit):
        Vehicle.__init__(self, start)
        self.gas = gas
        self.__gas_per_unit = gas_per_unit

    @property
    def gas_per_unit(self):
        print('a;sfj;asdfj')
        return self.__gas_per_unit

    @gas_per_unit.setter
    def gas_per_unit(self, gas_per_unit):
        self.__gas_per_unit = gas_per_unit

    def __gas_usage(self):
        return self.direction.length() * self.__gas_per_unit

    def movement(self, time):
        for i in range(time):
            if self.__gas_usage() <= self.gas:
                self.position = Point(self.position.x + self.direction.x, self.position.y + self.direction.y)
                self.gas -= self.__gas_usage()
                if self.is_recording:
                    self.path.append(self.position)
            else:
                print('топлива не хватит, заправимся? курс топлива', self.__gas_per_unit)
                self.gas += int(input())


car = Car(Point(0, 0), 100, 0.5)
car.direction = Vector(22, 22)
car.is_recording = True
car.gas_per_unit = 2

car.movement(10)
print(car.path)
print(car.gas)
