from src.intermediate_p1 import swap_key_value



def test_simple() :
    dict_a = {'a': 123, 'b': 456}
    res = swap_key_value(dict_a)

    assert res == {123: 'a', 456: 'b'}



def test_simple_tuple():
    dict_d = {'a': (6, 7, 8)}
    res = swap_key_value(dict_d)

    assert res == {(6,7,8) : 'a'}



def test_mutable_value() :
    dict_c = {'a': {'c': 123}}
    exception_is_thrown = False

    try :
        swap_key_value(dict_c)
    except ValueError :
        exception_is_thrown = True

    assert exception_is_thrown == True



def test_tuple_contains_mutable_types() :
    dict_b = {'a': (2, 3, [4])}
    exception_is_thrown = False

    try :
        swap_key_value(dict_b)
    except ValueError :
        exception_is_thrown = True

    assert exception_is_thrown == True


