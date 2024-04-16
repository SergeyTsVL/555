print('Задача 1: Фабрика Функций')
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.
# def maternal_function(n):
#     if n == 2:
#         def ff(x):
#             y = x + 2
#             return x * 2, y
#     elif n == 3:
#         def ff(x):
#             y = x - 2
#             return x * 3, y
#     else:
#         raise Exception('Аргумент n межет быть только 2 или 3 ')
#     return ff
# my_list = [10, 5, 1, 3, 48, 6, 1]
# a2 = maternal_function(2)
# a3 = maternal_function(3)
# # a9 = maternal_function(9)
# result = map(a2, my_list)
# print(list(result))
# result = map(a3, my_list)
# print(list(result))


def create_operation(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    else:
        return Exception('Error: Аргумент n межет быть только 2 или 3 ')

my_func_add = create_operation("add")
print(my_func_add(1,2))
my_func_subtract = create_operation("subtract")
print(my_func_subtract(1,2))
my_func_none = create_operation(2)
print(my_func_none)



print('Задача 2: Лямбда-Функции')
# Использовать лямбда-функцию для реализации простой операции и написать такую
# же функцию с использованием def. Например, возведение числа в квадрат

c = lambda x: x ** 2
print(c(2))

def cub(x):
    return x ** 2
print(cub(2))

print('Задача 3: Вызываемые Объекты')
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

class Rect():
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def __call__(self, scale):
        return f'Площадь: {scale * self.side_a * self.side_b} \nСтороны: {scale * self.side_a}, {scale *self.side_b}'


square = Rect(2,2)
res = square(1)
print(res)
