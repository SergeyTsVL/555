import os
import re
import requests
import csv
from airium import Airium


file_path = '../Price_List_Analyzer_Glob/Files_for_analysis'
file_html = '../Price_List_Analyzer_Glob/Files_for_analysis/output.html'
class PriceMachine():

    def __init__(self):
        self.data = []
    #     self.result = ''
    #     self.name_length = 0
    
    def load_prices(self):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        Product_name = ['товар', 'название', 'наименование', 'продукт']
        Name_with_price = ['розница', 'цена']
        Name_with_weight = ['вес', 'масса', 'фасовка']

        list_result = []

        files = os.listdir(file_path)
        for file in files:
            if "price" in file:
                with open(f'{file_path}/{file}', mode="r", encoding='utf-8') as sort_file:
                    for row in csv.reader(sort_file):
                        # print(row)

                        for i in Product_name:
                            try:
                                index_Product_name = row.index(i)
                                # print(f'Product_name {index_Product_name}')
                            except:
                                None
                        a = row[index_Product_name]

                        for i in Name_with_price:
                            try:
                                index_Name_with_price = row.index(i)
                                # print(f'Name_with_price {index_Name_with_price}')
                            except:
                                None
                        try:
                            b = int(row[index_Name_with_price])
                        except:
                            b = row[index_Name_with_price]

                        for i in Name_with_weight:
                            try:
                                index_Name_with_weight = row.index(i)
                                # print(f'Name_with_weight {index_Name_with_weight}')
                            except:
                                None
                        try:
                            c = int(row[index_Name_with_weight])
                        except:
                            c = row[index_Name_with_weight]

                        if a not in Product_name and b not in Name_with_price and c not in Name_with_weight:
                            result = a, b, c
                            list_result.append(result)
        list_result.sort(key=lambda x: x[1])
        print(list_result)

        return list_result


    def export_to_html(self):
        result = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        file = open(f"{file_html}", "w", encoding = 'utf-8')
        a = Airium()
        # Главное преимущество Airium – DOCTYPE уже включен!
        a('<!DOCTYPE html>')
        with a.html():
            with a.head():
                a.title(_t="Позиции продуктов")
            with a.body():
                with a.table():   # _t="Добро пожаловать на мою страницу!", id="intro"

                    with a.tr():
                        a.th(_t="Наименование")
                        a.th(_t="Цена")
                        a.th(_t="Масса")
                    with a.tr():
                        a.td()
                        pass
        print(str(a))
        file.write(str(a))

#     def find_text(self, text):
#
#
# pm = PriceMachine()
# print(pm.load_prices())
#
# '''
#     Логика работы программы
# '''
# print('the end')
# print(pm.export_to_html())
if __name__ == "__main__":
    data = PriceMachine.load_prices(file_path)
    data1 = PriceMachine.export_to_html(file_html)