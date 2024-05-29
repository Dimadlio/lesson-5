a=input("Введите любое слово: ")
a1=a.count("a")
a2=a.count("e")
a3=a.count("i")
a4=a.count("o")
a5=a.count("u")
b=a1+a2+a3+a4+a5
c=len(a)-b
print("Всего согласных в слове: ", c)
print("Всего гласных в слове: ", b)
if a1>0:
    print("Глассной a в слове: ", a1)
else:
    print("Глассной a в слове: False")
if a2>0:
    print("Глассной e в слове: ", a2)
else:
    print("Глассной e в слове: False")
if a3>0:
    print("Глассной i в слове: ", a3)
else:
    print("Глассной i в слове: False")
if a4>0:
    print("Глассной o в слове: ", a4)
else:
    print("Глассной o в слове: False")
if a5>0:
    print("Глассной u в слове: ", a5)
else:
    print("Глассной u в слове: False")