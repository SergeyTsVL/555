from random import randint


MAX_BUNCHES = 5

_holder = []

def put_stones():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))





def take_from_bunches(position, quantity):
    if 1 <= position <= len(_holder):
        _holder[position] -= quantity



def get_bunches():
    return _holder

def is_gemeover():
    return sum(_holder) == 0
