from env.src.main import divide


def test_divide():
    assert divide(a: 2, b: 1) == 2

    assert divide(a: 2, b: 0) == 0