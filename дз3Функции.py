import time



def decorater(func):
    def time_it(*args):
        print('ждать.')
        time.sleep(4)
        print('дождались')
        func(*args)

    return time_it


@decorater
def multiplication(*args):
    multi = 1
    for i in args:
        multi = multi * i
    print(multi)
    return str(multi)


print(multiplication(2, 3, 3, 3, 4, 5))
#почему он выводить None при return, но при print выводит нормальное число