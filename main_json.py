import json

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
# в зависимости от sort_type создаем файл под необходимым именем (сделал для своего удобства)
    if sort_type == 'firstName':
        file_name = f'employees_{sort_type}_sorted.json'
    if sort_type == 'lastName':
        file_name = f'employees_{sort_type}_sorted.json'
    if sort_type == 'department':
        file_name = f'employees_{sort_type}_sorted.json'
    if sort_type == 'salary':
        file_name = f'employees_{sort_type}_sorted.json'
# Выводим в созданный файл полученную структуру
    with open(file_name, "w") as sort_file1:
        json_employees_sorted1 = json.dump(dd, sort_file1, indent=4)
        return json_employees_sorted1

sort_type = 'firstName'

# Добавляем исключение
if sort_type in ['firstName', 'lastName', 'department', 'salary']:
    employees_rewrite(sort_type)
else:
    print(f'ValueError(\'Bad key for sorting\')')
