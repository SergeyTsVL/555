import unittest
from DZ_testy import Student


class RunningStudent(unittest.TestCase):
    def test_walk_10_times(self):
        d = Student('Вася')
        for i in range(1, 10, 1):
            d.walk()
        message = 'Дистанции не равны [дистанция человека Вася] != 500'
        self.assertEqual(d.walk(), 500, message)



    def test_run_10_times(self):
        d = Student('Коля')
        for i in range(1, 10, 1):
            d.run()
        message = 'Дистанции не равны [дистанция человека Коля] != 1000'
        self.assertEqual(d.run(), 1000, message)


    def test_competitions(self):
        d = Student('Коля')

        a = Student('Вася')
        for i in range(1, 10, 1):
            d.run()
            a.walk()
        message = '[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]'
        self.assertGreater(d.run(), a.walk(), message)



if __name__ == '__main__':
    unittest.main()

