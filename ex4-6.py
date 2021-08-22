class ElectronicsStorage:
    def __init__(self, dep_name, max_capacity):
        self.dep_name = dep_name
        try:
            self.max_capacity = int(max_capacity)
        except ValueError:
            print('Invalid data for maximum capacity')
        self.storage = []
        self.capacity = 0

    def take_units(self, name, model, number):
        if self.max_capacity - self.capacity >= number:
            self.storage.append({'Name': name, 'model': model, 'number': number})
            self.capacity += number
        else:
            print(f'Impossible to store {number} of {name}. Left space is {self.max_capacity - self.capacity}')

    def show_storage(self):
        data_to_show = str(self.storage).replace("{", "").replace("[", "").replace("]", "").replace("}, ", "\n").replace("}", "")
        return f'Current stock in {self.dep_name} is:\n{data_to_show}'

class Electronics:
    SKU_count = 0
    def __init__(self, name, model):
        self.name = name
        self.model = model
        Electronics.SKU_count += 1

    def enter_storage(self, department, number):
        try:
            department.take_units(self.name, self.model, int(number))
        except ValueError:
            print('The number must be number!')

class Printer(Electronics):
    def __init__(self, name, model, origin):
        self.origin = origin
        super().__init__(name, model)

class Scanner(Electronics):
    def __init__(self, name, model, origin):
        self.origin = origin
        super().__init__(name, model)

class Xerox(Electronics):
    def __init__(self, name, model, origin):
        self.origin = origin
        super().__init__(name, model)

sales = ElectronicsStorage('Sales', 10)
hr = ElectronicsStorage('HR', 5)
technics = ElectronicsStorage('Technics', 15)

hp = Printer('HP-3PL3', 'Printer', 'USA')
tencent = Scanner('Tencent-Magenta', 'Scanner', 'China')
xerox = Xerox('Xerox-3DD', 'Standard', 'Russia')

hp.enter_storage(hr, 5)
print(hr.show_storage())