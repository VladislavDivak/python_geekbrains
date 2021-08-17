class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, kg, depth):
        self.kg = kg
        self.depth = depth
        asphalt_mass = self._length * self._width * self.kg * self.depth
        return asphalt_mass

reinergasse = Road(5000, 30)
print(reinergasse._length)
print(reinergasse.calc_mass(5, 1))
