class Car:
    price = 1000000
    pover = 105

    def horse_powers(self):
        print('Цена авто:', self.pover, self.price)


class Nissan(Car):
    price = 5000
    pover = 205

class Kia(Car):
    def horse_powers(self):
        print('Цена авто:', self.pover + 100, self.price + 200000)


a = Car()
a.horse_powers()

s = Nissan()
s.horse_powers()

d = Kia()
d.horse_powers()


