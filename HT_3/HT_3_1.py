
#1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.

def square (num):

    return (4*num, num**2, (2*num**2)**.5)

 

result = square (int (input ("Введите сторону квадрата: ")))

print (result)