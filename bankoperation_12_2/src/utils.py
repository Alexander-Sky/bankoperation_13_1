"""
Модуль для работы с данными транзакций.
"""

import json
import logging
import os
from typing import Any, Dict, List

# Настройка логера для utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Создаем папку logs, если её нет
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Настройка file_handler
file_handler = logging.FileHandler(
    filename=os.path.join(log_dir, "utils.log"), mode="w", encoding="utf-8"  # перезаписываем при каждом запуске
)
file_handler.setLevel(logging.DEBUG)

# Настройка formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

# Добавляем handler к логеру
utils_logger.addHandler(file_handler)


def load_operations(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает операции из JSON-файла.

    Args:
        file_path: Путь к файлу с операциями

    Returns:
        List[Dict[str, Any]]: Список операций или пустой список в случае ошибки
    """
    utils_logger.debug(f"Попытка загрузки файла: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            utils_logger.info(f"Успешно загружено {len(data)} операций из {file_path}")
            return data
        else:
            utils_logger.warning(f"Файл {file_path} содержит не список, а {type(data)}")
            return []

    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except Exception as e:
        utils_logger.exception(f"Неожиданная ошибка при загрузке файла {file_path}: {e}")
        return []


def filter_operations_by_status(operations: List[Dict[str, Any]], status: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.

    Args:
        operations: Список операций
        status: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        List[Dict[str, Any]]: Отфильтрованный список операций
    """
    utils_logger.debug(f"Фильтрация операций по статусу: {status}")

    try:
        filtered = [op for op in operations if op.get("state") == status]
        utils_logger.info(f"Отфильтровано {len(filtered)} операций со статусом {status}")
        return filtered

    except Exception as e:
        utils_logger.exception(f"Ошибка при фильтрации операций: {e}")
        return []


def get_transaction_amount(transaction: Dict[str, Any]) -> float:
    """
    Получает сумму транзакции.

    Args:
        transaction: Транзакция

    Returns:
        float: Сумма транзакции
    """
    utils_logger.debug("Извлечение суммы из транзакции")

    try:
        amount = float(transaction.get("operationAmount", {}).get("amount", "0"))
        utils_logger.info(f"Успешно получена сумма: {amount}")
        return amount
    except (ValueError, TypeError, AttributeError) as e:
        utils_logger.error(f"Ошибка при получении суммы: {e}")
        return 0.0
