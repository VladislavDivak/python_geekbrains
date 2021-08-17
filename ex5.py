class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

tool1 = Stationery('Erich Krause')
tool2 = Pen('Bic')
tool3 = Pencil('Faber Castel')
tool4 = Handle('Molotow')

tool1.draw()
tool2.draw()
tool3.draw()
tool4.draw()