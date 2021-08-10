from itertools import count

while True:
    try:
        start_point = int(input('Give me a start number - '))
        end_point = int(input('Give me an end number - '))
        break
    except ValueError:
        print('Please, just give me a number')

for el in count(start_point):
    if el >= end_point + 1:
        break
    else:
        print(el)
