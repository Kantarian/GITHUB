#1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
  # Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
  # Логіка наступна:
   #    якщо введено коректну пару ім'я/пароль - вертається <True>;
   #    якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException






def name_password (name, password, silent = False):
  name = str(name)
  name_list = ['asd', 'dsa', 'zxc', 'cxz', 'qwe']
  password_list = [1,2,3,4,5]
  if name in name_list:
    if password in password_list:
      for i in range(len(name_list)):
        if name_list[i] == name and password_list[i] == password:
          return print('True')
        else:
          return print('False')
    else:
      return print('False')
  elif silent == True:
    return print('False')
  else:
    return print('False')




name_password ('asd',  1)