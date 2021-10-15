#task7
from itertools import count
from math import factorial

def fact(n):
    for i in count(1):
        yield factorial(i)
n = 0
stop = int(input("введите конечное число"))
for el in fact(n):
    if n < stop:
        print(el)
        n += 1
    else:
        break
