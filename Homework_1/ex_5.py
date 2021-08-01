rev = int(input('How much did you earn? '))
cost = int(input('How much did you spend? '))

profit = rev - cost

if profit < 0:
    print('You poor :(')
elif profit == 0:
    print('Perfectly balanced. As all things should be')
else:
    print(f'You earned! Profitability is {profit / rev}')
    pers = int(input('How much people you manage? '))
    print(f'Every employee has brought you {profit / pers} $')
