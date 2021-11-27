from collections.abc import Iterator


def product(number: int) -> Iterator:
    scam = 2
    while number > 1:
        if number % scam == 0:
            number = number / scam
            yield scam
        else:
            scam +=1
        if number == 1:
            return



c = product(55)
while True:
    print(next(c), end = ' ')