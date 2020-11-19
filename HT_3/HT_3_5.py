#5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.




def fibonacci(n):
	num = n + 1
	a = 0
	b = 1
	f_list =[]
	if n <= 0:
		print("Incorrect input")
	elif n == 1:
		f_list.append(1)
	else:
		for i in range(2,num):
			c = a + b
			a = b
			b = c
			if b <= n:
				f_list.append(b)
		return print(f_list)


fibonacci(9)

