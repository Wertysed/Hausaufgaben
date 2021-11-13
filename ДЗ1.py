class Driver:

    def __init__(self, name, time_one):
        self.name = name
        self.time_one = time_one
        self.all = sum(time_one)

    def __lt__(self, other):
        if isinstance(other, Driver):
            return self.all < other.all
        raise ValueError


n , m = [int(x) for x in input().split()]
drivers = []

for i in range(n):
    name = input()
    laps = [int(x) for x in input().split()]
    drivers.append(Driver(name, laps))

print(min(drivers).name)

