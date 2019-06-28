from src.beginner_p1 import flatten


def test_simple():
    fruit_list = ['apple', ['cherry', 'banana', ['kiwi', 'mango'], 'strawberry', 'orange'], 'lemon']
    numbers_list = [1, 2, [3, 4, 5, 6, 7], 8]

    a, b = flatten(fruit_list, numbers_list, 1)
    assert b == [1, 2, 3, 4, 5, 6, 7, 8]
    assert a == ['apple', 'cherry', 'banana', ['kiwi', 'mango'], 'strawberry', 'orange', 'lemon']


def test_more_lists():
    numbers_list = [1, 2, [3, 4, 5, 6, 7], 8, [9,10]]

    a, b = flatten([], numbers_list, 1)
    assert b == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_no_depth():
    fruit_list = ['apple', ['cherry', 'banana', ['kiwi', 'mango'], 'strawberry', 'orange'], 'lemon']

    a, b = flatten([], fruit_list, 0)
    assert b == ['apple', ['cherry', 'banana', ['kiwi', 'mango'], 'strawberry', 'orange'], 'lemon']


def test_epmty_list():
    a, b = flatten([], [], 2)
    assert a == []
    assert b == []


def test_negative_depth():
    numbers_list = [1, 2, [3, 4, 5, 6, 7], 8]

    a, b = flatten([], numbers_list, -1)
    assert a == []
    assert b == [1, 2, [3, 4, 5, 6, 7], 8]


