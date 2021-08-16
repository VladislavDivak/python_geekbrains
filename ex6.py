with open('ex6_text.txt', 'r', encoding='utf-8') as r_ex6:
    content = sum([i.split(': ') for i in r_ex6.readlines()], [])
    content = [i.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('\n', '') for i in content]
    for i in range(len(content)):
        if i % 2 != 0:
            content[i] = content[i].split(' ')
            content[i] = sum([int(j) for j in content[i]])
    dict_lessons = dict()
    for i in range(len(content)):
        if i % 2 == 0:
            lesson = {content[i]: content[i+1]}
            dict_lessons.update(lesson)

    print(dict_lessons)
