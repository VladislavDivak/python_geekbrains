from random import randint

numbers = [f'{str(randint(1, 100))} ' for el in range(10)]

with open('ex5_result.txt', 'w+') as w_ex5:
    w_ex5.writelines(numbers)
    w_ex5.seek(0)
    read_text = w_ex5.readlines()
    read_text = read_text[0].split(" ")
    read_text = [int(i) for i in read_text[:len(read_text)-1]]
    print(sum(read_text))
