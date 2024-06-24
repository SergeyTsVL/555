import time
import cv2

source = cv2.VideoCapture('../videos/video_BLUR_EYE.mp4')

while True:

    time.sleep(0.01)
    ret, img = source.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces.xml')
    results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=6)

    # нахожу среднюю арифметическую координат обоих глаз
    lx = []
    ly = []

    for (x, y, w, h) in results:
        a = str(x).split()
        s = ','.join(a)
        lx.append(int(s))

        a = str(y).split()
        s = ','.join(a)
        ly.append(int(s))

        sr_arf_lx = sum(lx) // 2
        sr_arf_ly = sum(ly) // 2

    for i in results:  # x, y, w, h - размеры квадрата выделяющего лица
        # заблюрил изображение взгляда
        img[sr_arf_ly - 10: sr_arf_ly + h, sr_arf_lx - 40: sr_arf_lx + w + 60] = (
            cv2.GaussianBlur(img[sr_arf_ly - 10: sr_arf_ly + h, sr_arf_lx - 40: sr_arf_lx + w + 60],
                                                                     (41, 41), 0))
        # разделяем изображение на несколько слоев
        r, g, b = cv2.split(img[sr_arf_ly - 10: sr_arf_ly + h, sr_arf_lx - 40: sr_arf_lx + w + 60])

        # указываем порядок отображения слоев, можно отображать по отдельности
        img[sr_arf_ly - 10: sr_arf_ly + h, sr_arf_lx - 40: sr_arf_lx + w + 60] = cv2.merge([g, g, g])

    cv2.imshow("Result", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
source.release()



