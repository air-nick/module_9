# Даны два списка
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для first_result:
# Используем zip для объединения списков попарно и вычисляем разницу длин строк,
# если длины не равны.
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для second_result:
# Используем range и len для перебора индексов и сравниваем длины строк
# на одинаковых позициях в списках.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))  # Преобразуем генератор в список для вывода
print(list(second_result))  # Преобразуем генератор в список для вывода
