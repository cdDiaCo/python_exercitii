

def swap_key_value(dictionary) :
    new_dict = {}

    for elem in dictionary :
        new_key = dictionary[elem]
        new_dict[new_key] = elem

    print(new_dict)
    return new_dict



def is_swap_possible(data_struct) :

    res = True

    for element in data_struct :
        if isinstance(data_struct, dict):
            element = data_struct[element]

        if isinstance(element, dict) or isinstance(element, list) or isinstance(element, set) :
            # element is mutable and swap not possible
            res = False
        else :
            if isinstance(element, tuple) : # recursively check every tuple element
                return is_swap_possible(element)

    print(res)
    return res



dict_a = {'a': 123, 'b': 456}
dict_b = {'a': (2,3,[4])}
dict_c = {'a': {'c': 123}}
dict_d = {'a' : (6,7,8)}


if is_swap_possible(dict_d) :
    swap_key_value(dict_d)





