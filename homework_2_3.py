# task 3
print("Проверка через список и словарь - время года на выходе будет дублироваться")
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
num = int(input("Введите номер месяца(число)"))
if num in winter :
    print("Зима")
    c = 1
elif num in spring :
    print("Весна")
    c = 2
elif num in summer :
    print("Лето")
    c = 3
elif num in autumn :
    print("Осень")
    c = 4
else:
    print("Такого месяца нет в году")
    c = 0
season = {"Зима": 1, "Весна": 2, "Лето": 3, "Осень": 4}
for element in season:
    if c == season[element]:
        print(element)
