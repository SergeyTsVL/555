# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
import os
import time
directory = 'C:/Windows/help'
path_normalized = os.path.normpath(directory)
count = 0
for root, dirs, files in os.walk(directory):
    print('*' * 27)
    print(root, dirs, files)
    print(os.path.dirname(root))
    print(os.path.dirname(__file__))
    print(os.path.getsize(root))
    count += len(files)
    for file in files:
        filepath = os.path.join(root, file)
        secs = os.path.getctime(filepath)
        filetime = time.gmtime(secs)

        if filetime[0] == 2013:
            print(filepath, secs)
        # formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(directory)
        parent_dir = os.path.dirname(__file__)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}')
        print(os.path.dirname(filepath))

print(count)




