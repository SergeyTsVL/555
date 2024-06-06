from datetime import datetime
class SuperDate(datetime):

    def get_season(self):

        if a.month in [12, 1, 2]:
            return 'Winter'
        if a.month in [3, 4, 5]:
            return 'Spring'
        if a.month in [6, 7, 8]:
            return 'Summer'
        if a.month in [9, 10, 11]:
            return 'Autumn'

    def get_time_of_day(self):

        if a.hour in range(6, 12):
            return 'Morning'
        if a.hour in range(12, 18):
            return 'Day'
        if a.hour in range(18, 24):
            return 'Evening'
        if a.hour in range(0, 6):
            return 'Night'

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
