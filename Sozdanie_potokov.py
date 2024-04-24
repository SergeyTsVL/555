import time
import random
from threading import Thread

# from collections import defauldict

english_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
numbers_10 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')


def creating_stream(args):
    for i in range(len(args)):
        ff = random.choice(args)
        print(ff)
        time.sleep(0.1)
    print("fglkjlkjj")


# creating_stream(args=english_letters)


thread = Thread(args=english_letters)
thread.start()
creating_stream(args=numbers_10)
thread.join()
