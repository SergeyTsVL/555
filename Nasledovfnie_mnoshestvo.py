class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000
        self.pover = 105

    def horse_powers(self):
        return self.pover

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 5000
        self.vehicle_type = 'yes'

    def horse_powers(self):
        print('Цена авто:', self.pover + 100, self.price + 100000)

a = Nissan()
print(a.vehicle_type, a.price)
a.horse_powers()
