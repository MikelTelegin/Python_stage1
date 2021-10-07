#task 1
def my_func1 (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "нельзя делить на 0"
    except ValueError:
        return "можно вводить только числа"
print(my_func1(int(input("Введите делимое число")), int(input("Введите делитель"))))
