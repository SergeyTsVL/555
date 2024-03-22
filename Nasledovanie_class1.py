class Car:

    def __init__(self, pover):
        self.price = 1000000
        self.pover = pover

    def horse_powers(self):
        return self.pover

class Nissan(Car):

    def __init__(self, pover):
        super().__init__(pover)
        self.price = 15000000


    def horse_powers(self):
        print('Цена авто:', self.pover + 100, self.price + 200000)
class Kia(Car):

    def horse_powers(self):
        print('Цена авто:', self.pover + 200, self.price + 400000)


a = Car(100)
a.horse_powers()

s = Nissan(200)
s.horse_powers()

d = Kia(300)
d.horse_powers()


