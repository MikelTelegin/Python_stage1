def my_func3(x, y, z):
    massiv = [x, y, z]
    minimum = min(massiv)
    massiv.remove(minimum)
    print(sum(massiv))
my_func3(10, -5, 2)
