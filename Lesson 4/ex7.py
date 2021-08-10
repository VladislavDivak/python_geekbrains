def generator(n):
    for el in range(1, n+1):
        yield el

while True:
    try:
        n = int(input('Give me a number - '))
        break
    except ValueError:
        print('Please, just give me a number')

g = generator(n)

i = 1
result = 1
for el in g:
    result = el * result
    print(f'{el}! = {result}')
    i += 1

