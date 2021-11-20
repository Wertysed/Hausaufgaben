def multiplication(*args):
    multi = 1
    for i in args:
        multi = multi * i
    return multi


print(multiplication(2, 212, 1244, 12, 33))
