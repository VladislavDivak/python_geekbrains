my_list = [1, 300, 42, 3, 24, 532, 23, 54, 2, 1, 9435, 2, 55, 3, 433, 3422]

new_list = [sub2 for sub1, sub2 in zip(my_list, my_list[1:]) if int(sub1) < int(sub2)]

print(my_list)
print(new_list)