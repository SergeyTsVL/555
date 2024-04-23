import warnings

salary_recipients = ['Иванов Иван Иванович', 'Петров Петор Петрович', 'Сидоров Сидор Сидрович',
                     'Пушкин Александр Сергеевич', 'Дантес Жорж Шарль', 'Маяковский Владимир Владимирович',
                     'Гагарин Юрий Алексеевич']
salary = ['15000', '15000', '15000', '45500', '13200', '38000', '55000', '55000']


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        dictionary = {}
        for key, val in result:
            dictionary.setdefault(key, val)
        if len(salary_recipients) > len(salary):
            warnings.warn('Список получателей зарплаты больше списка назначенных выплат', UserWarning)
        if len(salary_recipients) < len(salary):
            warnings.warn('Список получателей зарплаты меньше списка назначенных выплат', UserWarning)
        if len(salary_recipients) > len(set(salary_recipients)):
            warnings.warn('В списке получателей ЗП повторяются работники', UserWarning)
        return dictionary
    return wrapper
@is_prime
def sum_three(*args):
    list_of_salary_recipients = list(zip(*args))
    return list_of_salary_recipients

result = sum_three(salary_recipients, salary)
# print(result)
for name, age in result.items():
    print(f'{name:<35} {age}')