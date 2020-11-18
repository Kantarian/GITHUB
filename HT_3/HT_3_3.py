#3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000, и яка вертатиме True, якщо це число просте, и False - якщо ні.



def prime(n) : 

	if (n <= 1) : 
		return print('False')
	if (n <= 3) : 
		return print ('True')

	if (n % 2 == 0 or n % 3 == 0) : 
		return print('False')

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return print('False')
		i = i + 6

	return print('True')


prime(998)
	

