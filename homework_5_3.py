#task 3
with open("task_3.txt", "r") as file_obj:
    names = []
    salary = []
    my_list = file_obj.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            names.append(i[0])
            salary.append(i[1])
print(f"Оклад меньше 20.000 {names}, средний оклад {sum(map(int, salary)) / len(salary)}")
