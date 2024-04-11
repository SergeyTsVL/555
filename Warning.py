import warnings
def hyperbole(a):
    list = []
    i = 1
    while a > 0.0001:
        if a > 0.01:
            a = a / i
            i += 1
            print(a)
        else:
            print('Принт приближаемся к нулю')
            a = a / i
            i += 1
            print(a)
        list.append(a)
    print(list)

s = hyperbole(1)
print(s)

try:
    (list[-1] - 0.01) ** 0.5 != True
except:
    print('UserWarning')