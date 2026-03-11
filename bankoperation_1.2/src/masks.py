def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по формату XXXX XX** **** XXXX
    """
    # Удаляем пробелы и проверяем
    card_str = str(card_number).replace(" ", "")
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по формату **XXXX
    """
    # Удаляем пробелы и проверяем
    account_str = str(account_number).replace(" ", "")
    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_str[-4:]}"
