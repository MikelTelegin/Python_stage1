#task 4 (1)
def my_func(x, y):
    return x ** y
print(my_func(2, -3))

#task 4 (2)
def my_func2(x, y):
    res = 1/x
    z = abs(y)-1
    while z>0 :
        res = res/x
        z = z-1
    return res
print(my_func2(2, -3))
