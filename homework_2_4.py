# task 4
words = []
words = input("Введите строку из слов, разделяя слова пробелами")
print(words)
words = words.split()
print(words)
for i, el in enumerate(words, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
