def my_func(var_1, var_2, var_3):
    variables = [var_1, var_2, var_3]
    variables.remove(min(variables))
    result = sum(variables)
    return result

while True:
    try:
        first_num = int(input("Give me the first number - "))
        second_num = int(input("Give me the second number - "))
        third_num = int(input("Give me the third number - "))
        break
    except ValueError:
        print('All numbers must be numbers, dude')

print(f'The result is {my_func(first_num, second_num, third_num)}')

