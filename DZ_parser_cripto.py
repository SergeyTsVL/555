from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/ru/'
response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')
i = 0

list_ = []
for p in data.find_all('tr'):
    i += 1
    title = p.text
    list_.append(title)
print(list_)

for i, title in enumerate(list_):
    new = title.replace('$', '$')
    list_[i] = new
    print(i + 1, new)




