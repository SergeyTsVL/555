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
            try:
                warnings.warn('Это важное предупреждение, значение меньше 0,001', UserWarning)
            except UserWarning as e:
                print(f'Предупреждение перехвачено как {e}')
            a = a / i
            i += 1
            print(a)
        list.append(a)
    # print(list)
# warnings.simplefilter('error', UserWarning)
# warnings.simplefilter('ignore', UserWarning)

s = hyperbole(1)
print(s)

