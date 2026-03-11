from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по статусу

    :param data: список словарей с операциями
    :param state: значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список операций
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате

    :param data: список словарей с операциями
    :param descending: флаг сортировки по убыванию (True - убывание, False - возрастание)
    :return: отсортированный список операций
    """
    # Для работы с датой будем использовать строковое сравнение
    return sorted(data, key=lambda x: x["date"], reverse=descending)
