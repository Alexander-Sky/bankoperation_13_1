from src.processing import filter_by_state, sort_by_date


# Тесты для filter_by_state
def test_filter_by_state(test_data):
    # Проверяем фильтрацию по умолчанию (EXECUTED)
    result_executed = filter_by_state(test_data)
    assert len(result_executed) == 2
    assert all(item["state"] == "EXECUTED" for item in result_executed)

    # Проверяем фильтрацию по CANCELED
    result_canceled = filter_by_state(test_data, "CANCELED")
    assert len(result_canceled) == 2
    assert all(item["state"] == "CANCELED" for item in result_canceled)


# Тесты для sort_by_date
def test_sort_by_date(test_data):
    # Ожидаемый порядок при сортировке по убыванию
    expected_desc = [
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572",
    ]

    # Ожидаемый порядок при сортировке по возрастанию
    expected_asc = [
        "2018-06-30T02:08:58.425572",
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
        "2019-07-03T18:35:29.512364",
    ]

    # Проверяем сортировку по убыванию
    result_desc = sort_by_date(test_data)
    assert [item["date"] for item in result_desc] == expected_desc

    # Проверяем сортировку по возрастанию
    result_asc = sort_by_date(test_data, False)
    assert [item["date"] for item in result_asc] == expected_asc
