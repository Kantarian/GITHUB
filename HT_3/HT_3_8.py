#8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня -
#  пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
  #Наприклад:
       #fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       #fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]




def rotate (l, n):
    return print(l[n:] + l[:n])
l = [1,2,3,4,5]
rotate(l,1)
rotate(l,-2)
