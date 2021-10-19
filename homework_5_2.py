#task 2
my_list = ["Москва\n", "Санкт-Петербург\n", "Сочи\n"]
with open("task_2.txt", "w") as file_obj:
    file_obj.writelines(my_list)
with open("task_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} символов в строке")
    print(f"Количество строк {lines}")
