# def test(*args):
#     print("Распечатывает параметры внутри: ", args)
# test(1, 5, True, "sdfvsed", 217)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_mines_1 = factorial(n=n-1)
    return n * factorial_n_mines_1
print(factorial(int(input("Введите число "))))


