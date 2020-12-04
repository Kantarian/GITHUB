#3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 3: 
		print('length should be at least 3') 
		val = False
		
	if len(passwd) > 8: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 


def name_check(username): 
	val = True
	
	if len(username) < 3: 
		print('length should be at least 3') 
		val = False
		
	if len(username) > 50: 
		print('length should be not be greater than 50') 
		val = False

	if val: 
		return val 

def main():
    passwd=['Geek12@','Geek12','Geek@','Geek','Geek12@tr']
    username=['username','as']
    for name in username: 
        for passw in passwd:
            if password_check(passw) and name_check(name):
                print(f''' 
                name: {name}
                password: {passw}
                Status: ok
                ''') 
            if not name_check(name):
                print(f''' 
                name: {name}
                password: {passw}
                Status: Invalid Username!
                ''')
            if not (password_check(passw) and name_check(name)):
                print(f''' 
                name: {name}
                password: {passw}
                Status: Invalid Username and Password!
                ''')        
            else:
                print(f''' 
                name: {name}
                password: {passw}
                Status: Invalid Password!
                ''')





main() 