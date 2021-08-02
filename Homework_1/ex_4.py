num = int(input('Give me the number - '))

max_digit = 1
a = 1
n = 1

while a != 0:
    a = (num // n)
    b = a % 10
    if b > max_digit:
        max_digit = b
    n = n * 10

print(f'The max digit is - {max_digit}')