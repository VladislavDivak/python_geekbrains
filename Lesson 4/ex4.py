from random import randint

my_list = [randint(1, 10) for el in range(1, 21)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print('Original list: ', my_list)
print('Processed list: ', new_list)
