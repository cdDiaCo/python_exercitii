from src.compare_dictionaries_file import compare_dictionaries


def test_false(): # the second dictionary is bigger
    first_dict = {'b':10, 'c':11, 'f': 32}
    second_dict = {'s':22, 'k':76, 'o':44}
    result = compare_dictionaries(first_dict, second_dict)

    assert result == False


def test_true(): # the second dictionary is smaller
    first_dict = {'s':22, 'k':76, 'o':44}
    second_dict = {'b':10, 'c':11, 'f': 32}
    result = compare_dictionaries(first_dict, second_dict)

    assert result == True


def test_equal_values_false(): # dictionaries have equal values but the second one is bigger
    first_dict = {'s':22, 'k':10, 'o':11}
    second_dict = {'b':10, 'c':44, 'f': 32}
    result = compare_dictionaries(first_dict, second_dict)

    assert result == False


def test_equal_values_true(): # dictionaries have equal values but the second one is smaller
    first_dict = {'b':10, 'c':44, 'f': 32}
    second_dict = {'s':22, 'k':10, 'o':11}
    result = compare_dictionaries(first_dict, second_dict)

    assert result == True





