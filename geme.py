from nim_angine import put_stones, take_from_bunches, get_bunches, is_gemeover
from termcolor import cprint, colored

put_stones()
user_number = 1

while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда берем?', color=user_color))
    qua = input(colored('Сколько берем?', color=user_color))
    take_from_bunches(position=int(pos), quantity=int(qua))
    if is_gemeover():
        break
    user_number = 2 if user_number == 1 else 1
print("Выиграл игрок номер", user_number)


