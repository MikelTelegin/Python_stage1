#task1 
def salary():
    time = input("Введите количество часов: ")
    money = input("Введите ставку за 1 час: ")
    extra = input("Введите размер премии - ")
    try:
        time = float(time)
        money = float(money)
        extra = float(extra)
        res = time * money + extra
        print(f"Размер зарплаты: {res}")
    except ValueError:
        print("Допустимо вводить только числа")
salary()
