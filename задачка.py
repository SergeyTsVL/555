# a = int(input("Введите число"))
# b = a * 2
# print("Ответ:", b)


print('Введите координаты начала отрезка')
ax = int(input('ax='))
bx = int(input('bx='))
print('Введите координаты конца отрезка')
ay = int(input('ay='))
by = int(input('by='))
d = (((ax + bx) ** 2) + ((ay + by) ** 2)) ** 0.5
print('Длинна отрезка по заданным координатам равна', d)
