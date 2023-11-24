class Transport:
    def _init_(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class Autobus(Transport):
    pass

autobus = Autobus("Renaul Logan", 180, 12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.speed} Пробег: {autobus.mileage}")
