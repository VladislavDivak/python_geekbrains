def summarize(arg_list):
    user_list = arg_list.split(' ')
    user_list = map(int, user_list)
    sum_result = sum(user_list)
    return sum_result

result = 0
while True:
    user_input = input("To exit the program press 'Q'\nEnter any numbers separated by space - ").lower()
    if user_input.find('q') >= 0:
        user_input = user_input.replace('q', '0')
        result = result + summarize(user_input)
        print(f'The final sum of the entered numbers is - {result}')
        break
    else:
        result = result + summarize(user_input)
        print(f'The sum of the entered numbers is - {result}')





