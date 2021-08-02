true_password = 'qwerty'
num_attempt = 3

user_password = input('Enter password -')
while True:
    if user_password == true_password:
        print('Access granted')
        break

    else:
        num_attempt = num_attempt - 1

    if num_attempt != 0:
        print(f'Wrong password. Try again\n {num_attempt}')
        user_password = input('Enter password -')
        continue

    print('Fuck off')
    break
