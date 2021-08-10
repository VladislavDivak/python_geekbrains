from itertools import cycle

my_mom_words = ['Хватить сидеть за компуктером!']
print(my_mom_words[0])
while True:
    try:
        end_point = int(input('Сколько можно повторять??? '))
        break
    except ValueError:
        print('Нет, ты скажи нормально, сколько можно повторять???')

i = 0
for el in cycle(my_mom_words):
    if i >= end_point:
        break
    else:
        print(el)
        i += 1

