#5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
#-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
#-  Повиннi опрацювати такi умови:
#-  x > y;       вiдповiдь - х бiльше нiж у на z
#-  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z


x = int(input('Input start range of year:'))
y = int(input('Input end range of year:'))
def diff(x,y):
   
    if x == y:
        unswer = f'вiдповiдь - х дорiвнює y'
    elif x < y:
        z = y - x
        unswer = f'вiдповiдь - у бiльше нiж х на {z}'

    elif x > y:
        z = x - y
        unswer = f'вiдповiдь - х бiльше нiж у на {z}'
    return unswer


print(diff(x,y))