class Cellule:
    def __init__(self, name, cells):
        self.name = name
        self.cells = int(cells)

    def __add__(self, object):
        return f'{self.name} ate {object.name} and now have {self.cells + object.cells} cells'

    def __sub__(self, object):
        if self.cells > object.cells:
            return f'Now there are {self.cells - object.cells} cells in the {self.name}'
        else:
            return f'Both cells died :('

    def __mul__(self, object):
        new_cell = Cellule(input('Give the name to the new created cell - '), self.cells * object.cells)
        return f'{new_cell.name} was created with {new_cell.cells} cells'

    def __truediv__(self, object):
        new_cell = Cellule(input('Give the name to the new created cell - '), self.cells / object.cells)
        return f'{new_cell.name} was created with {new_cell.cells} cells'

    def make_order(self, cells_in_row):
        count = self.cells
        result = ''
        while True:
            if count >= cells_in_row:
                result += f'{"*" * cells_in_row}\n'
            else:
                result += f'{"*" * count}\n'
                break
            count -= cells_in_row
        return f'{result}'

cell1 = Cellule('George', 10)
cell2 = Cellule('Tom', 5)

print(cell1.make_order(3))
