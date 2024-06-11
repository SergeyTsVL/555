import json
import re

def employees_rewrite(sort_type):
    with open("employees.json", "r") as sort_file:
        json_employees_sorted = json.load(sort_file)
# создаем отсортированный список после "employees"
        sorting_list = []
        for i in json_employees_sorted["employees"]:
            k = i[sort_type]
            sorting_list.append(k)
        sorting_list.sort()
        sorted_list = []
        for i in sorting_list:
            for j in json_employees_sorted["employees"]:
                k = j[sort_type]
                if i == k:
                    sorted_list.append(j)
# объединяем "employees" и отсортированный список
        dd = dict()
        dd['employees'] = dd.setdefault('employees', []) + sorted_list

# Выводим в созданный файл полученную структуру
    with open(file_name, "w") as sort_file1:
        json_employees_sorted1 = json.dump(dd, sort_file1, indent=4)
        return json_employees_sorted1

sort_type = 'salary'   # задаем sort_type

# в зависимости от sort_type создаем файл под необходимым именем (сделал для своего удобства) + сверяем с pattern
if sort_type == 'firstName':
    pattern = r'[fF][iI][rR][sS][Tt][nN][aA][mM][Ee]'
    file_name = f'employees_{sort_type}_sorted.json'
if sort_type == 'lastName':
    pattern = r'[lL][aA][sS][tT][nN][aA][mM][eE]'
    file_name = f'employees_{sort_type}_sorted.json'
if sort_type == 'department':
    pattern = r'[dD][eE][pP][aA][rR][tT][mM][eE][nN][tT]'
    file_name = f'employees_{sort_type}_sorted.json'
if sort_type == 'salary':
    pattern = r'[sS][aA][lL][aA][rR][yY]'
    file_name = f'employees_{sort_type}_sorted.json'

# проверяем на сооответствие с регулярными выражениями
sample = re.findall(pattern, sort_type)
sample_sort_type = ''.join(sample)
print(sample_sort_type)

# Добавляем исключение
if sort_type in sample_sort_type:
    employees_rewrite(sort_type)
else:
    print(f'ValueError(\'Bad key for sorting\')')
