from collections import defaultdict
import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, skills, enemies, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skills = skills
        self.enemies = enemies

    def run(self):
        print(f'{self.name}, на нас напали!')

        for skill in range(0, self.enemies, self.skills):
            self.enemies -= self.skills
            time.sleep(0.1)
            print(f'{self.name}, сражается {int(skill / self.skills) + 1} день(дня)..., осталось {self.enemies} воинов.')
        if self.enemies <= 0:
            print(f'{self.name} одержал победу спустя {int(skill / self.skills) + 1} дней')


knight1 = Knight("Sir Lancelot", 10, 100) # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20, 100) # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')