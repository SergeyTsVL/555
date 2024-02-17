a = int(input('Переменная а = '))
b = int(input('Переменная b = '))
print(a, b)
def test(a, b):
    return a, b
pover = test(a=int(input('Переменная а = ')), b=int(input('Переменная b = ')))
print(pover)


i = 1
j = 2
z = 3
print(i, j, z)
def test2(i, j, z):
    return i, j, z
pover2 = test2(i=10, j=20, z=30)
print(pover2)