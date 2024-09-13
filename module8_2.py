def personal_sum(numbers):
    if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
        raise TypeError("Некорректный тип данных для подсчёта суммы")

    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)  # Преобразуем к float для учета int и float
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return (result, incorrect_data)


def calculate_average(numbers):
    try:
        # Вызов функции personal_sum для получения суммы и количества некорректных данных
        total_sum, _ = personal_sum(numbers)
        # Подсчет среднего арифметического
        count = len([item for item in numbers if isinstance(item, (int, float))])
        if count == 0:
            return 0
        return total_sum / count
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        return 0


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать