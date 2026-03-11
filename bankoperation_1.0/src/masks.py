def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты по формату XXXX XX** **** XXXX

    Args:
        card_number: Номер карты (число или строка из цифр)

    Returns:
        str: Замаскированный номер карты

    Examples:
        >>> get_mask_card_number(7000792289606361)
        '7000 79** **** 6361'
        >>> get_mask_card_number("7000 7922 8960 6361")
        '7000 79** **** 6361'
    """
    # Преобразуем в строку и удаляем всё, кроме цифр
    card_str = str(card_number).replace(" ", "")

    # Проверяем, что остались только цифры
    if not card_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # Проверяем длину
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формируем маску
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер банковского счета по формату **XXXX

    Args:
        account_number: Номер счета (число или строка из цифр)

    Returns:
        str: Замаскированный номер счета

    Examples:
        >>> get_mask_account(73654108430135874305)
        '**4305'
        >>> get_mask_account("7365 4108 4301 3587 4305")
        '**4305'
    """
    # Преобразуем в строку и удаляем всё, кроме цифр
    account_str = str(account_number).replace(" ", "")

    # Проверяем, что остались только цифры
    if not account_str.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    # Формируем маску (последние 4 цифры)
    masked = f"**{account_str[-4:]}"
    return masked
