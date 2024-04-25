import threading
import time
import random

def number():
    numbers_10 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    for i in range(10):
        ff = random.choice(numbers_10)
        time.sleep(1)
        print(ff)

def letters():
    english_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    for i in range(10):
        pp = random.choice(english_letters)
        time.sleep(1)
        print(pp)

thread_1 = threading.Thread(target=number)
thread_2 = threading.Thread(target=letters)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
