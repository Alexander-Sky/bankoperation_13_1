from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    if "Счет" in input_string.lower():
        parts = input_string.split()
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        parts = input_string.split()
        card_type = " ".join(parts[:-1])
        card_number = parts[-1]
        try:
            masked_number = get_mask_card_number(card_number)
        except ValueError:
            raise ValueError("Неверный формат номера карты")
        return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ
    """
    return date_string[:10].replace("-", ".")
