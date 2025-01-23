def apply_all_func(int_list, *functions):
    # Создаём пустой словарь для результатов
    results = {}

    # Перебираем переданные функции
    for func in functions:
        # Добавляем результат работы функции в словарь
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results

# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
# Ожидаемый результат: {'max': 20, 'min': 6}

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Ожидаемый результат: {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
