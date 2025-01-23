# Даны списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Создание списка с длинами строк из first_strings, где длина >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Создание списка кортежей слов одинаковой длины из двух списков
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# 3. Создание словаря из строк объединённых списков, где длина строки чётная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результата
print(first_result)
print(second_result)
print(third_result)
