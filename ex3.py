class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt

input_data = []
while True:
    try:
        element = input('Enter a number: ')
        if element.lower() == 'stop':
            print('Program is finished')
            print(f'Your list is {input_data}')
            break
        try:
            number = int(element)
        except ValueError:
            raise OwnException('Please enter only numbers')
    except OwnException as err:
        print(err)
    else:
        input_data.append(number)
        print(input_data)





