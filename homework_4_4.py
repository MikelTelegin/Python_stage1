#task4
list = [randint(0, 10) for i in range(10)]
print(list)
res = [i for i in list if list.count(i) == 1]
print(res)
