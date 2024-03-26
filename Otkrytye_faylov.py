from pprint import pprint

text_name = 'Text_1.txt'
text = open(text_name, mode='rb')
text_content = text.read()

pprint(text_content)

text.close()
