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