user_input = input('Tell me something - ')
list = user_input.split()

for ind, el in enumerate(list,1):
        print(ind,el[:10])