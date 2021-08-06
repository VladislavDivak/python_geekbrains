def int_func(word):
    return word.capitalize()

user_word = input('Give me a word - ')
user_word = int_func(user_word)
print(user_word)

user_text = input('Now give me a couple of words separated by space - ')
user_text = user_text.split(' ')
user_cap_text = []
for el in user_text:
    user_cap_text.append(int_func(el))
print(' '.join(user_cap_text))
