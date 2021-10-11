#task6
from itertools import count, cycle

def my_count(start, stop):
    for i in count(start):
        if i > stop:
            break
        else:
            print(i)

def my_cycle(list, iter):
    i = 0
    a = cycle(list)
    while i < iter:
        print(next(a))
        i += 1
        
my_count(start = int(input("Введите начальное число")), stop = int(input("введите конечное число")))
my_cycle(list = [1, 2, 3], iter = int(input("Введите число элементов")))
