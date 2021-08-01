a = int(input('How much do you run now? '))
b = int(input("What's your target? "))

n = 1.1
day = 1
while a < b:
    a = a * n
    day = day + 1

print(f'You will reach your target after {day} days')