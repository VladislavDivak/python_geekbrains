from functools import reduce


def multiply(par1, par2):
    return par1 * par2

my_list = [el for el in range(100, 1001) if el % 2 == 0]
result = (reduce(multiply, my_list))

print('Original list: ', my_list)
print('Result: ', result)
