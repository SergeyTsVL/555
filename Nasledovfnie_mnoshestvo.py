class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000
    pover = 105

    def horse_powers(self):
        print('Цена авто:', self.pover, self.price)

class Nissan(Car, Vehicle):
    vehicle_type = "yes"
    price = 25252
    def horse_powers(self):
        print('Цена авто:', self.pover + 100, self.price + 100000)

a = Nissan()
print(a.vehicle_type, a.price)
print(a.horse_powers)
