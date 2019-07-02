from src.beginner_p2 import merge_two_objects

def test_simple():
    a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

    new_obj = merge_two_objects(a, b)
    assert new_obj == {'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}


def test_different_length():
    a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3])}
    b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

    new_obj = merge_two_objects(a, b)
    assert new_obj == {'x': [1, 2, 3, 4, 5, 6], 'y': 5, 'z': set([1, 2, 3, 4]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}


def test_keys_not_matching():
    a = {'a': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'b': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

    new_obj = merge_two_objects(a, b)
    assert new_obj == {'a': [1, 2, 3], 'y': 5, 'z': set([1, 2, 3, 4]), 'b': 'qweqwe', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer"), 'x': [4, 5, 6], 'w': 'asdf'}


def test_keys_matching_but_different_order():
    a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    b = {'y': 4, 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer", 'x': [4, 5, 6], 'z': set([4, 2, 3])}

    new_obj = merge_two_objects(a, b)
    assert new_obj == {'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}





