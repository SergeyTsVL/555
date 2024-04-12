def ff_2(x):
    return x % 2

def ff_22(x):
    return x ** 2

list1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = map(ff_22, filter(ff_2, list1))
print(list(result))

