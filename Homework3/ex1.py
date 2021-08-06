def my_division (a, b):
    a, b = int(a), int(b)
    return print(a / b)
while True:
    a = input('Give me the first number - ')
    b = input('Give me the second number - ')
    if a.isdigit() and b.isdigit() and int(b) != 0:
        my_division(a, b)
        break
    else:
        print("Error")



