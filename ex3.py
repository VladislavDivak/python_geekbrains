with open("ex3_salaries.txt", "r") as r_ex3:
    content = r_ex3.readlines()
    content = ": ".join(content).replace("\n", "").split(": ")
    names = [content[i] for i in range(0, len(content), 2)]
    salaries = [int(content[i]) for i in range(1, len(content), 2)]
    i = 0
    for i in range(0, len(salaries)):
        if salaries[i] <= 20000:
            print(f'{names[i]} earns less than 20,000 rub')
        i += 1
    print('Average salary is ', sum(salaries)/len(salaries))
