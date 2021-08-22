class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = str(input("Введите два числа через запятую: "))

try:
    inp_data = list(map(int, inp_data.split(',')))
    if inp_data[1] == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_data[0]/inp_data[1]}")