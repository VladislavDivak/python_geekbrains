from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def message(self):
        print(f'I am the Clothing {self.name}, wear me!')

class Coat(Clothing):
    def __init__(self, name, V):
        super().__init__(name)
        self.size = V

    @property
    def fabric(self):
        return f'{self.size / 6.5 + 0.5} m2'

    def message(self):
        print(f'I am the Coat {self.name}, wear me!')

class Taxedo(Clothing):
    def __init__(self, name, H):
        super().__init__(name)
        self.height = H

    @property
    def fabric(self):
        return f'{2 * self.height + 0.3} m2'

    def message(self):
        print(f'I am the Taxedo {self.name}, wear me!')

clothing1 = Coat('Zara', 4)
clothing2 = Taxedo('Kenzo', 2)

print(clothing1.fabric, clothing2.fabric)