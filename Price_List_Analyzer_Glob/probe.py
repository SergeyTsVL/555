import os
import re
import requests
import csv
# https://drive.google.com/file/d/1-GQlpOxlc4n5Js3aQe7XJC1mGxrEdHro/view?usp=sharing

directory = 'C:/Users/tsars/PycharmProjects/pythonProject1/Price_List_Analyzer_Glob/Files_for_analysis'
files = os.listdir(directory)
files_prise = []
# print(files)

Product_name = ['товар', 'название', 'наименование', 'продукт']
Name_with_price = ['розница', 'цена']
Name_with_weight = ['вес', 'масса', 'фасовка']


list_result = []

for file in files:
    if "price" in file:
        with open(f'{directory}/{file}', mode="r", encoding='utf-8') as sort_file:
            for row in csv.reader(sort_file):
                # print(row)
                # return

                for i in Product_name:
                    try:
                        index_Product_name = row.index(i)
                        print(f'Product_name {index_Product_name}')
                    except:
                        None
                a = row[index_Product_name]

                for i in Name_with_price:
                    try:
                        index_Name_with_price = row.index(i)
                        print(f'Name_with_price {index_Name_with_price}')
                    except:
                        None
                b = row[index_Name_with_price]

                for i in Name_with_weight:
                    try:
                        index_Name_with_weight = row.index(i)
                        print(f'Name_with_weight {index_Name_with_weight}')
                    except:
                        None
                c = row[index_Name_with_weight]

                if a not in Product_name and b not in Name_with_price and c not in Name_with_weight:
                    result = a, b, c
                    list_result.append(result)
                # print('********')
print(list_result)




    # response = requests.get(f"{directory}/{file}")
    #
    # pattern = r'http[s:][:/](?:[_0-9а-яА-Яa-zA-Z/.-]){1,100}[x\_][\d]{1,10}[.][gjp][ping][egf][gf\'\"\.\/\* ]'
    # for i in re.findall(pattern, response.text):
    #     print(i)
