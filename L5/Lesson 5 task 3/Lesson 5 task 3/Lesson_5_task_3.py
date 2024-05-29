x=int(input("Введите минимальную сумму инвестиций: "))
a=int(input("Долларов у Майкла для инвестиций: "))
b=int(input("Долларов у Ивана для инвестиций: "))
if (a>=x) and (b>=x):
    print(2)
elif (a>=x) and (b<x):
    print("Mike")
elif (a<x) and (b>=x):
    print("Ivan")
elif (a<x) and (b<x) and (a+b<x):
    print(0)
elif (a<x) and (b<x) and (a+b>=x):
    print(1)
