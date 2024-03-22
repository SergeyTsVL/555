class Car:
    price = 1000000
    pover = 105
    def __init__(self, price, pover):
        self.price = price
        self.pover = pover

    def horse_powers(self):
        return self.price

class Nissan(Car):

    def __init__(self, price, pover):
        # Car.__init__(self, price)
        self.price = price
        self.pover = pover

    def horse_powers(self):
        print('Цена авто:', self.pover + 100, self.price + 200000)
class Kia(Car):

    def horse_powers(self):
        print('Цена авто:', self.pover + 200, self.price + 400000)


a = Car()
a.horse_powers()

s = Nissan()
s.horse_powers()

d = Kia()
d.horse_powers()


