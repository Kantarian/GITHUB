#1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
  # Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
  # Логіка наступна:
   #    якщо введено коректну пару ім'я/пароль - вертається <True>;
   #    якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException






def name_password (name, password, silent = False):
  name = str(name)
  name_list = ['asd', 'dsa', 'zxc', 'cxz', 'qwe']
  password_list = [1,2,3,4,5]
  status = None
  if name in name_list:
    for i in range(len(name_list)):
        if name_list[i] == name and password_list[i] == password:
          print('True')
          status = True
          break
        else:
          print('Password incorrect')
          status = False
          break
  else:
    print ('Users not found')
    status = False
  while True:
    try:
      if status == False and silent == False:
        raise Exception
      if status == False and silent == True:
        print('False')
        return (False)
        break
      if status == True and silent == True:
        print('True. Login Successful')
        return (True)
        break
      if status == True and silent == False:
        print('True Login Successful')
        return (True)
        break
    except Exception as LoginException:
      print('something went wrong')
      break      
    else:
      break





name_password ('asd', 2, False)


