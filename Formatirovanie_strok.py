#Использование %:
team1_num = 5
print("В команде Мастера кода участников: %d!" % (team1_num))

team2_num = 6
print("Итого сегодня в командах участников: %d, %d!" % (team1_num, team2_num))

# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач:{0:1d}!'.format(score_2))

team1_time = 18015.2
print('Волшебники данных решили задачи за {0:0.1f} c !'.format(team1_time))

# Использование f-строк:
score_1 = 44
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

team2_time = 12115.2
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
print(f"Результат битвы: {result}")

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:0.1f} секунды на задачу!.")