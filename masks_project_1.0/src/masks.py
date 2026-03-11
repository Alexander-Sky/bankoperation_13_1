def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по формату XXXX XX** **** XXXX
    """
    # Преобразуем число в строку
    card_str = str(card_number)
    # Проверяем длину
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    # Формируем маску
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по формату **XXXX
    """
    # Преобразуем число в строку

    account_str = str(account_number)
    # Формируем маску
    masked = f"**{account_str[-4:]}"
    return masked
