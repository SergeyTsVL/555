import zipfile
from pprint import pprint

# zip_file_name = 'voyna-i-mir-tom-1.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# # zipfile.printdir()
# for filename in zfile.namelist():
#     # print(filename)
#     zfile.extract(filename)

filename = 'voyna-i-mir-tom-1.zip'
stat = {}
# stat = {'а':{'т': 500, 'х': 5, }, 'т':{'о': 100, 'у': 50, },}
prev_char = ''
with open(filename, 'r', encoding='cp1251') as file:
    for line in file:
        print(line)
        for char in line:
            if prev_char in stat:
                if char in stat[prev_char]:
                    stat[prev_char][char] += 1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char][char] = {char: 1}
pprint(stat)
