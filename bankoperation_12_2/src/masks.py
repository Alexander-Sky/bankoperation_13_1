"""
Модуль для маскировки банковских карт и счетов.
"""

import logging
import os
from typing import Union

# Настройка логера для masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Создаем папку logs, если её нет
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Настройка file_handler
file_handler = logging.FileHandler(
    filename=os.path.join(log_dir, "masks.log"), mode="w", encoding="utf-8"  # перезаписываем при каждом запуске
)
file_handler.setLevel(logging.DEBUG)

# Настройка formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

# Добавляем handler к логеру
masks_logger.addHandler(file_handler)


def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Маскирует номер банковского счета по формату ** XXXX.
    """
    masks_logger.debug(f"Начало маскировки номера счета: ...{str(account_number)[-4:]}")

    try:
        account_str = str(account_number).replace(" ", "")

        if len(account_str) < 4:
            masks_logger.error(f"Неверный формат номера счета: {account_str}")
            raise ValueError("Номер счета должен содержать минимум 4 символа")

        masked = f"** {account_str[-4:]}"
        masks_logger.info(f"Успешно замаскирован номер счета: {masked}")
        return masked

    except Exception as e:
        masks_logger.exception(f"Ошибка при маскировке счета: {e}")
        raise
