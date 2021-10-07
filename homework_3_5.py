#task 5
def my_summ():
    result = 0
    while True:
        line = input("Введите суммируемые числа через пробел, для получения суммы нажмите enter, для остановки программы нажмите q")
        numbers = line.split()
        for i in numbers:
            if i == "q":
                return result
            else:
                try:
                    i = float(i)
                    result += i
                except ValueError:
                    print("Ошибка ввода - нужно вводить только числа.")
        print(f"Сумма равна {result}")
print(my_summ())
