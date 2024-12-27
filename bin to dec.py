B = input('enter the binary number: ')
p = 0
d = 0
while B:
    last_digit = int(B[-1])

    d += last_digit*(2**p)

    B = B[:-1]

    p += 1

print(f'decimal value of  is {d}')
    
