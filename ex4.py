class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def stop(self):
        print('Car has stopped')

    def go(self):
        print('Car started to drive')

    def turn(self, direction):
        self.direction = direction
        print(f'Car has turned {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed is exceeded on {self.speed - 60}')
        else:
            super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed is exceeded on {self.speed - 40}')
        else:
            super().show_speed()

class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            print(f'Speed is exceeded on {self.speed - 100}')
        else:
            super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

car1 = TownCar(50, 'black', 'Mazda')
car2 = WorkCar(50, 'white', 'BMW')
car3 = PoliceCar(60, 'blue', 'Lada')

print(car1.show_speed())
print(car2.show_speed())
print(car3.is_police)