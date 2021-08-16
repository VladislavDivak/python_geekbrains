eng = ['One', 'Two', 'Three', 'Four']
rus = ['Один', 'Два', 'Три', 'Четыре']
new_content = []

with open('ex4_text.txt', 'r') as r_ex4:
    for i in range(0, len(eng)):
        new_content.append(r_ex4.readline().replace(eng[i], rus[i]))
    r_ex4.seek(0)
    for i in range(0, len(eng)):
        print(r_ex4.readline().replace(eng[i], rus[i]), end="")

with open("ex4_text_rus.txt", 'w', encoding='utf-8') as w_ex4:
    w_ex4.writelines(new_content)
