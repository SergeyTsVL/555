import cv2
import numpy as np

img = cv2.imread('Kartyncka.jpg')


new_img = np.zeros(img.shape, dtype='uint8') # создаем  матрицу с каждым числом 0. Прописываем ее размеры

img - cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.GaussianBlur(img, (3, 3), 0)  # размытие изображения указываем только нечетные числа

img = cv2.Canny(img, 50, 50)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_LIST-получаем все доступные контуры

cv2.drawContours(new_img, con[:374], -1, (230, 11, 148), 1)
cv2.drawContours(new_img, con[374:755], -1, (0, 0, 255), 1)
cv2.drawContours(new_img, con[755:], -1, (0, 255, 0), 1)

cv2.imshow('Result', new_img)
cv2.waitKey(0)


