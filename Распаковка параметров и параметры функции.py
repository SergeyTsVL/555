#def print_params(a = 1, b = 'строка', c = True):
#    return a, b, c
#ff = print_params(a=1, b='строка', c=True)
#print("Функция вывела параметры", ff)


#def print_params(a = 1, b = 'строка', c = True):
#    return a, b, c
#ff = print_params(a=1, b='строка', c=True, g = 25)
#print("Функция вывела параметры", ff)


#def print_params(a = 1, b = 'строка', c = True):
#    return a, b, c
#ff = print_params(a=1, b='строка')
#print("Функция вывела параметры", ff)


#def print_params():
#    return
#ff = print_params()
#print("Функция вывела параметры", ff)


#def print_params(a = 1, b = 'строка', c = True):
#    return a, b, c
#ff = print_params(b = 25)
#print("Функция вывела параметры", ff)


def print_params(a = 1, b = 'строка', c = True):
    return a, b, c
ff = print_params(c=[1, 2, 3])
print("Функция вывела параметры", ff)



values_list = [5, "отлично", float]
values_dict = {"a" : 10, "b" : 'буква', "c" : True}
res = print_params(**values_dict)
res2 = print_params(*values_list)
print(res)
print(res2)

values_list_2 = [45, "броня"]
res3 = print_params(*values_list_2, 42)
print(res3)



