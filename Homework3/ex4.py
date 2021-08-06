# def my_func(x, y):
#     """Вариант решения с **"""
#     result = x ** y
#     return result

def my_func(x, y):
    """Вариант решения ерез цикл"""
    result = x
    for i in range(1, -y):
        result = x * x
        i += 1
    return 1/result

while True:
    try:
        first_num = float(input("Введите действительное число (основание степени) - "))
        second_num = int(input("Введите целое отрицательное число (степень) - "))
        if second_num >= 0:
            print('Ошибка. Степень должна быть меньше нуля по условию')
            continue
        else:
            break
    except ValueError:
        print('Ошибка. Введите корректные значения')

print(f'Результат {my_func(first_num, second_num)}')

