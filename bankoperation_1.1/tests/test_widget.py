from src.widget import get_date, mask_account_card


def test_mask_account_card_visa():
    # Тест для карты Visa
    input_data = "Visa Platinum 7000792289606361"
    expected = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(input_data) == expected


def test_mask_account_card_maestro():
    # Тест для карты Maestro
    input_data = "Maestro 1596837868705199"
    expected = "Maestro 1596 83** **** 5199"
    assert mask_account_card(input_data) == expected


def test_mask_account_card_account():
    # Тест для счета
    input_data = "Счет 73654108430135874305"
    expected = "Счет **4305"
    assert mask_account_card(input_data) == expected


def test_get_date():
    # Тест для преобразования даты
    input_date = "2024-03-11T02:26:18.671407"
    expected = "11.03.2024"
    assert get_date(input_date) == expected


def test_get_date_another():
    # Дополнительный тест для даты
    input_date = "2023-12-25T12:00:00"
    expected = "25.12.2023"
    assert get_date(input_date) == expected
