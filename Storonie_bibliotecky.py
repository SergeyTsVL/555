# **********************requests*****requests******requests******************

# import requests
# req = requests.get('https://cms-assets.tutsplus.com/cdn-cgi/image/width=850/uploads/users/1251/posts/28204/image/Forest_Background_Optimized.jpg', stream=True)
# req.raise_for_status()
# with open('Forest.jpg', 'wb') as fd:
#     for chunk in req.iter_content(chunk_size=50000):
#         print('Received a Chunk')
#         fd.write(chunk)
#
# import requests
# req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
# req.raise_for_status()
# with open('Nanotechnology.html', 'wb') as fd:
#     for chunk in req.iter_content(chunk_size=50000):
#         fd.write(chunk)

# import requests
# # делаем запрос на чтение страницы https://sky.pro/media/
# response = requests.get( 'https://sky.pro/media/' )
# # print(response.ok)
# # проверяем, успешен ли запрос
# print(response.text)
# # выводим полученный ответ на экран

# import requests
# response = requests.options('https://httpbin.org')  # Метод OPTIONS нужен, чтобы спросить сервер о том, какие методы поддерживает ресурс.
# print(response.text)  # будет пустым
# print(response.headers['Allow'])  # 'HEAD, GET, OPTIONS'

# import requests
# response = requests.get('https://httpbin.org/get')
# print(response.text)
# # GET — самый распространённый HTTP-метод. Его используют для чтения интернет-ресурса.

# import requests
# data_response = requests.post('https://httpbin.org/post', data={'foo': 'bar'})
# print(data_response.text)  # переданные данные находятся по ключу form
# json_response = requests.post('https://httpbin.org/post', json={'foo': 'bar'})
# print(data_response.text)  # ключ form пустой, теперь данные лежат в json
# # Метод POST используют для отправки на сервер данных, которые передаются в теле запроса.

# import requests
# response = requests.get('https://httpbin.org/head')
# print(response.text)  # ответ будет пустым
# print(response.headers)
# # Этот метод очень похож на GET — с той лишь разницей, что HEAD возвращает пустое тело ответа.
# # Он нужен, когда нужно посмотреть только на заголовки, не загружая ответ целиком.

# import requests
# response = requests.put('https://httpbin.org/put', data={'foo': 'bar'})
# print(response.text)
# # Метод PUT очень похож на POST — с той разницей, что несколько последовательных
# # вызовов PUT должны приводить к одному и тому же результату.

# import requests
# response = requests.patch('https://httpbin.org/patch', data={'foo': 'bar'})
# print(response.text)
# # PATCH аналогичен методу POST, но с двумя отличиями: он используется для частичных изменений
# # ресурса и его нельзя использовать в HTML-формах.

# import requests
# response = requests.delete('https://httpbin.org/delete')
# print(response.text)
# # Метод используется для удаления ресурса. Поддерживает передачу данных, однако не требует её:
# # тело запроса может быть пустым.

# *****************************pandas***pandas***pandas****************************
#
# import pandas as pd
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "City": ["New York", "San Francisco", "Los Angeles"]
# }
# df = pd.DataFrame(data)
# print(df)
# # DataFrame – это основной объект pandas, который представляет собой
# # двумерную таблицу с метками на строках и колонках.
# print('*' * 30)
#
# df = pd.read_csv("output.csv")
# print(df)
# # Чтобы загрузить данные из файла, например, CSV, используйте следующую функцию:
# print('*-' * 30)
#
# print(df.head())
# # Посмотрим на первые 5 строк нашего DataFrame:
# print('*' * 30)
#
# print(df["Name"])
# # Выберем определенную колонку:
# print('*' * 30)
#
# print(df.loc[1])
# # Выберем строки по индексу:
# print('*' * 30)
#
# print(df["Age"].mean())
# # С помощью pandas можно легко агрегировать данные. Например, посчитаем средний возраст:
# print('*' * 30)
#
# print(df["Age"].min())
# print(df["Age"].max())
# # найдем минимальное и максимальное значение
# print('*' * 30)
#
# df.to_csv("output.csv", index=False)
# # сохранить ваш DataFrame в файл, например, в формате CSV,
# print('*' * 30)

# ********************NumPy******NumPy******NumPy*****************
#
# import numpy as np
#
# X = np.array([[7, 8, 9], [10, 11, 12], [10, 11, 12]])
# print(X)
# # Переделать список в NumPy-массивы
# print('*' * 30)
#
# Y = X.copy()
# print(Y)
# # Сделать копию
# print('*' * 30)
#
# A = np.zeros((3, 3))
# print(A)
# # Сделать нулевой или единичный вариант определенного размера.
#
# B = np.ones((3, 2))
# print(B)
# print('*' * 30)
#
# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.zeros_like(A)
# print(B)
# # Использовать примеры из библиотеки
# print('*' * 30)
#
# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.ones_like(A)
# print(B)
# # Использовать примеры из библиотеки
# print('*' * 30)
#
# A = np.zeros((2, 3), 'int')
# print(A)
# # В третьем методе размеры передавались одним параметром (кортеж размеров).
# # Вторым (в способах № 3 и № 4) можно указать желаемый тип элементов.
#
# B = np.ones((3, 2), 'complex')
# print(B)
# print('*' * 30)
# *************************************************************
#
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line Plot')
#
# plt.show()
# #  это популярная библиотека для создания статических, интерактивных и анимированных визуализаций на Python.
# #  С помощью Matplotlib вы можете создавать графики, диаграммы, гистограммы и многое другое.

# ********************************************************************************
# from PIL import Image, ImageFilter
#
# image = Image.open('Forest.jpg')
# blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.save('blurred_example.jpg')
# это библиотека для работы с изображениями. Она позволяет открывать, изменять и сохранять изображения
# в различных форматах. Некоторые возможности Pillow включают изменение размера изображения, поворот,
# наложение фильтров и т.д.

# ********************************************************
# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((255, 255, 255))
#     pygame.draw.circle(screen, (0, 0, 255), (400, 300), 50)
#     pygame.display.flip()
#
# pygame.quit()
# # это кросс-платформенная библиотека для создания видеоигр и мультимедийных приложений на Python. Она предоставляет
# # возможности для работы с графикой, звуком, управлением и столкновениями объектов.


