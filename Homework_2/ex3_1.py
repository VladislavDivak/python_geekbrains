#Вариант с использованием list
seasons = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']

while True:
    try:
        user_month = int(input('Give me the number of the month - '))
        if user_month <= 12:
            break
        print('Seriously? There are only 12 months, not more!')
    except ValueError:
        print('Just put the number, dude')

print(f'The month is in {seasons[user_month - 1]}')