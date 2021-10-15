#task5
from functools import reduce
list = [i for i in range(100, 1001) if i % 2 == 0]
def mult_func(a, b):
    return a * b

print(reduce(mult_func, list))
