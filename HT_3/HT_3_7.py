#7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.


def repeat(num): 
    repeated = [] 
    for i in range(len(num)): 
        k = i + 1
        for j in range(k, len(num)): 
            if num[i] == num[j]: 
                repeated.append(num[i]) 
    return len(repeated)
  
list1 = [1, 2, 3, 2, 2, 3, 4,  
         5, -2, 6, 6, -2, -2] 
print (repeat(list1)) 

