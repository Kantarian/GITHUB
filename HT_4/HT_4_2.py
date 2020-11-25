#2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
 #  - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
 #  - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
 #  - щось своє :)
 #  Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.



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
	passwd = 'Geek12@'
	username = 'username'
	
	if (password_check(passwd) and name_check(username)): 
		print("Password and Username is valid") 
	if not name_check(username): 
		print("Invalid Username!") 
	else: 
		print("Invalid Password!") 
		
	 
if __name__ == '__main__': 
	main() 
