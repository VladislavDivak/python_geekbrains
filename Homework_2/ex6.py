inventory = []
i = 0

while True:
    item_dict = dict(name='a', price=0, amount=0, UoM='a')
    new_name = dict(name=input('Enter the name of the product - '))
    item_dict.update(new_name)
    while True:
        try:
            new_price = dict(price=int(input('Enter the price of the product - ')))
            break
        except ValueError:
            print('Just put the number, dude')
    item_dict.update(new_price)
    while True:
        try:
            new_amount = dict(amount=int(input('Enter the amount of the product - ')))
            break
        except ValueError:
            print('Just put the number, dude')
    item_dict.update(new_amount)
    new_UoM = dict(UoM=input('Enter the unit of measure of the product - '))
    item_dict.update(new_UoM)
    inventory.insert(i, (i+1, item_dict))
    i = i + 1
    q_cont = input('Do you want to enter more items? y/n - ')
    if q_cont == 'n':
        break

print(f'Your initial inventory - \n {inventory}')

new_inventory = zip(*inventory)
char_inventory = list(new_inventory)[1]
name = list()
price = list()
amount = list()
UoM = list()

for el in char_inventory:
    name.append(dict(el).get('name'))
    price.append(dict(el).get('price'))
    amount.append(dict(el).get('amount'))
    UoM.append(dict(el).get('UoM'))

result = dict(name=name, price=price, amount=amount, UoM=UoM)

print(f'Result of compilation - \n {result}')
