#task2
from random import randint
list = [randint(-10, 10) for i in range(10)]
print(list)
res = [i for i in list if i > list[list.index(i)-1]]
print(res)
