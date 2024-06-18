import cv2
import numpy as np

a = 400
photo = np.zeros((a, a, 3), dtype='uint8')

# градиентное закрашивание
for i in range(a):
    cv2.line(photo, (i, 0), (i, a), ((250 / a) * i, (250 / a) * i, (250 / a) * i), thickness=a // 400)

# создание круга
cv2.circle(photo, (a // 2, a // 2), a // 8, (119, 201, 105), thickness=a // 400 * 3)
cv2.circle(photo, (a // 2, a // 2), a // 16, (119, 201, 105), thickness=a // 400 * 3)

# градиентное закрашивание для получения полукругов
for i in range(a):
    cv2.line(photo, (i, 0), (i, a // 2), ((250 / a) * i, (250 / a) * i, (250 / a) * i), thickness=a // 400)

# создание круга
cv2.circle(photo, (photo.shape[0] // 2, a // 2), (a // 8 * 3), (250, 250, 250), thickness=a // 400 * 3)

# создание линии
cv2.line(photo, (a // 8 * 3, a // 8 * 4), (a // 16 * 6, a // 16 * 6), (219, 31, 26), thickness=a // 400 * 3)
cv2.line(photo, (a // 16 * 7, a // 16 * 8), (a // 16 * 7, a // 16 * 6), (219, 31, 26), thickness=a // 400 * 3)
cv2.line(photo, (a // 16 * 9, a // 16 * 8), (a // 16 * 9, a // 16 * 6), (219, 31, 26), thickness=a // 400 * 3)
cv2.line(photo, (a // 16 * 10, a // 16 * 8), (a // 16 * 10, a // 16 * 6), (219, 31, 26), thickness=a // 400 * 3)

cv2.line(photo, (a // 16 * 6, a // 16 * 6), (a // 16 * 7, a // 16 * 6), (26, 31, 219), thickness=a // 400 * 3)
cv2.line(photo, (a // 16 * 9, a // 16 * 6), (a // 16 * 10, a // 16 * 6), (26, 31, 219), thickness=a // 400 * 3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
