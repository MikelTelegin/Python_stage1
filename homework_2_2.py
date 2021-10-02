# task 2
changelist = []
while True :
    b = input("Введите элемент списка, для выхода нажмите stop ")
    if b.title() == "Stop" :
        break
    changelist.append(b)
print(changelist)        
i = 1
while i < len(changelist) :
    changelist[i], changelist[i-1] = changelist[i-1], changelist[i]
    i += 2
print(changelist)
