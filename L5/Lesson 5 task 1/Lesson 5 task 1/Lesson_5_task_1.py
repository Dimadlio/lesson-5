number=int(input("Введите число: "))
if number==0:
    print("Нулевое число")
elif (number%2==0) and (number>0):
    print("Четное положительное число")
elif (number%2==0) and (number<0):
    print("Четное отрицательное число")
elif(number%2!=0) and (number>0):
    print("Нечётное положительное число")
elif(number%2!=0) and (number<0):
    print("Нечётное отрицательное число")
