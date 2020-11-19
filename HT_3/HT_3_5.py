#5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.




def fibonacci(n):
	num = n + 2
	a = 0
	b = 1
	f_list =[0]
	if n < 0:
		return print("Incorrect input")
	elif n == 0:
		return print(f_list)
	elif n == 1:
		return print([0,1])	
	else:
		f_list = [0,1]
		for i in range(2,num):
			c = a + b
			a = b
			b = c
			if b <= n:
				f_list.append(b)
		return print(f_list)


fibonacci(1)


