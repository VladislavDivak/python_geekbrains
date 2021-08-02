sec = int(input('Give me a number, my dude - '))

hh = sec // 3600
mm = (sec // 60) % 60
ss = sec % 60

print(f'{hh:02}:{mm:02}:{ss:02}')
