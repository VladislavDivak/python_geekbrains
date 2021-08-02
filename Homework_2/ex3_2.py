#Вариант с использованием dict
seasons = {'Winter': [12, 1, 2],
           'Spring': [3, 4, 5],
           'Summer': [6, 7, 8],
           'Autumn': [9, 10, 11]}

seasons_keys = list(seasons.keys())
seasons_vals = sum(list(seasons.values()),[])

while True:
    try:
        user_month = int(input('Give me the number of the month - '))
        if user_month <= 12:
            break
        print('Seriously? There are only 12 months, not more!')
    except ValueError:
        print('Just put the number, dude')

month = seasons_vals.index(user_month) // 3

print(f'The month is in {seasons_keys[month]}')