with open('ex2_test.txt', 'r') as r_ex2:
    content_str = r_ex2.readlines()
    content_words = " ".join(content_str)
    print('Number of strings: ', len(content_str))
    print('Number of words: ', len(content_words.split(' ')))

