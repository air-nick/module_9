def all_variants(text):
    """Генератор, который возвращает все подпоследовательности переданной строки"""
    length = len(text)

    # Перебираем все возможные длины подстрок
    for size in range(1, length + 1):
        # Перебираем все подстроки данной длины
        for start in range(length - size + 1):
            yield text[start:start + size]  # Используем yield для возврата результата


# Пример вызова
a = all_variants("abc")

for i in a:
    print(i)
