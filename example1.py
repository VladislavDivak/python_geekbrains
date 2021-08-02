# Узнать тип данных

num = 1
print(type(num))

f_num = 1.5
print(type(f_num))

data = 'Secret'
print(type(data))

# Арифметические операции с числовыми типами данных

a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b) #целочисленное деление
print(a % b) #целый остаток от деления


# Операции со строками

data='Hello world'
text='Moscow'

new_text = data + text
print(new_text)

long_data = data * 100
print(long_data)

#Логические операции
c = 4
print(a < b and a == c)

#Ввод-вывод данных и явное преобразование типов

# Сложна
# number_1 = input('Введите первое число - ')
# number_2 = input('Введите второе число - ')
#
# number_1 = int(number_1)
# number_2 = int(number_2)
#
# result = number_1 + number_2
# print(result, type(number_1), type(number_2))

#легко
number_1 = int(input('Введите первое число - '))
number_2 = int(input('Введите второе число - '))

result = number_1 + number_2
print(result, type(number_1), type(number_2))

# условные конструкции

true_password = 'qwerty'
user_password = input('Введите пароль - ')

if true_password == user_password:
    print('Access approved')
else: print('Access denied')

#Цикл

k = 1
while k < 10:
    print(k)
    k = k + 1

