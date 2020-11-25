#6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#   P.S. Повинен вертатись генератор.
#   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range


def range_2 (num, start = 0, step = 1):
    i = start
    range_2_list = []
    while i < num:
        range_2_list.append(i)
        i = i + step
    return print (range_2_list)
        
range_2(10,1,2)

def myRange(start, stop=None, step=None):

    if stop == None:
        stop = start

    if step == None:
        step = 1

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ('%g' % start)
        start = start + step
        break

    lyst = myRange(start, stop=None, step=None)
    for num in lyst:
        print(num)

print(myRange(0, 10, 2)) 