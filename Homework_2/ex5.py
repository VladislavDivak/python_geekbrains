my_list = [7, 5, 3, 3, 2]

while True:
    try:
        new_el = int(input('Give me the number - '))
        break
    except ValueError:
        print('Just put the number, dude')

for el in my_list:
    if new_el > el:
        my_list.insert(my_list.index(el),new_el)
        break

# my_list.append(new_el)
# my_list.sort()
# my_list.reverse()

print(my_list)