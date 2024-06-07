import requests
import re

response = requests.get('https://sky.pro/media/')

pattern = r'http[s:][:/](?:[_0-9а-яА-Яa-zA-Z/.-]){1,100}[x\_][\d]{1,10}[.][gjp][ping][egf][gf\'\"\.\/\* ]'

# , где http[s:][:/] - описание URL-адресов, (?:[_0-9а-яА-Яa-zA-Z/.-]){1,100} - промежуточные символы до расширения
# [x\_][\d]{1,10} - размеры картинки, для исключения неполных адресов,
# [.][gjp][ping][egf][gf\'\"\.\/\* ]' - расширениями .jpg, .jpeg, .png или .gif.

for i in re.findall(pattern, response.text):
    print(i)

