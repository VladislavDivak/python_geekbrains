with open("ex1_result.txt", "w+") as w_test_ex1:
    while True:
        user_input = input("To exit the program press 'Enter'\nEnter the string - ")
        if user_input == '':
            break
        else:
            w_test_ex1.write(user_input)
            w_test_ex1.write("\n")
    w_test_ex1.seek(0)
    print(w_test_ex1.read())
