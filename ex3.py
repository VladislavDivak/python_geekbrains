class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Full name of the worker: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income of the worker: {sum(self._income.values())}')

worker_1 = Position('Vasya', 'Pupkin', 'Doctor', 50000, 25000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())

