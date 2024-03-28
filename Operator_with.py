from pprint import pprint

text_name = 'Text_1.txt'
with open(text_name, mode='rb') as text:
    text_content = text.read()

pprint(text_content)

print(text.close())

