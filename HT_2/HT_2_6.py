#6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя


test_string = "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
def MEGA_strings(test_string):
    if 30 <= len(test_string) <= 50:
        res = [int(i) for i in test_string if i.isdigit()] 
        print ("The original len string : " + str(len(test_string)))
        print ("The number of letters in the string is : " + str(len(test_string)-len(res)))
        print ("The number of numbers in the string is : " + str(len(res)))

    elif 30 > len(test_string):
        print ('your fantasy')

    elif 50 < len(test_string):
        res = [int(i) for i in test_string if i.isdigit()] 
        res_2 = 0
        for num in res:
            res_2 = res_2 + num
        print("The sum of numbers in the string is : " + str(res_2))
        res_3 = [str(i) for i in test_string if not i.isdigit()] 
        strings = ''
        for string in res_3:
            strings = strings + string
        print(strings)    
        

print(MEGA_strings(test_string))

