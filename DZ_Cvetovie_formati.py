import cv2
import numpy as np
import dload

image = dload.save("https://static.tildacdn.com/tild3331-6133-4263-b364-633561333339/color_text.jpg",
                   overwrite=False)

img = cv2.imread(image)
new_img = np.zeros(img.shape, dtype='uint8') # создаем  матрицу с каждым числом 0. Прописываем ее размеры

img - cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.GaussianBlur(img, (3, 3), 0)  # размытие изображения указываем только нечетные числа

img = cv2.Canny(img, 50, 50)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_LIST-получаем все доступные контуры

cv2.drawContours(new_img, con[:382], -1, (230, 11, 148), 1)
cv2.drawContours(new_img, con[382:773], -1, (0, 0, 255), 1)
cv2.drawContours(new_img, con[773:], -1, (0, 255, 0), 1)

# kernel = np.ones((1, 1), np.uint8)
# new_img = cv2.dilate(new_img, kernel, iterations=0)
#
# new_img = cv2.erode(new_img, kernel, iterations=0)  # из жирных линий делаем тонкие

cv2.imshow('Result', new_img[0:500, 0:750])
cv2.waitKey(0)
