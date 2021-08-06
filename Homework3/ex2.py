def pers_data():
    questions = ['name', 'surname', 'year of birth', 'city', 'email', 'phone']
    characteristics = list()
    for el in questions:
        characteristic = input(f'Please insert your {el} - ')
        characteristics.append(characteristic)
    return print(f'Your data:\n{" ".join(characteristics)}')

my_data = pers_data()

print(my_data)
