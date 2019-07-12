

def swap_key_value(dictionary) :
    new_dict = {}

    for elem in dictionary :
        if is_swap_possible(dictionary[elem]) :
            new_key = dictionary[elem]
            new_dict[new_key] = elem
        else :
            raise ValueError('Mutable value found. Swapping not possible')

    print(new_dict)
    return new_dict



def is_swap_possible(element) :
    res = True

    if isinstance(element, (dict, list, set)) :
        # element is mutable and swap not possible
        res = False
    elif isinstance(element, tuple) : # recursively check every tuple element
        for el in element :
            if not is_swap_possible(el): # if at least one element in the tuple is mutable - return false
                return False

    return res


dict_a = {'a': 123, 'b': 456}
dict_b = {'a': (2,3,[4])}
dict_c = {'a': {'c': 123}}
dict_d = {'a' : (6,7,8)}


try :
    swap_key_value(dict_d)
except ValueError as err:
    print(err)






