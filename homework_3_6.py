#task 6
def int_func():
    wordsline = input("Введите слова маленькими буквами через пробел. По окончании ввода нажмите enter").split()
    new = []
    for word in wordsline:
        word = word.title()
        new.append(word)
    res = " ".join(new)
    print(res)
int_func()
