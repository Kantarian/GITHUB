#5. Write a script to convert decimal to hexadecimal
        #Sample decimal number: 30, 4
        #Expected output: 1e, 04

while True:
    d = int(input('Input a decimal: '))
    h = format(d, '02x')
    print('Hexadecimal: ',h)
    
