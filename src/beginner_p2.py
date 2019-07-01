
from itertools import zip_longest


def merge_two_objects(obj1, obj2):
    new_obj = {}
    obj1_keys = obj1.keys()
    obj2_keys = obj2.keys()
    for (key1, value1), (key2, value2) in zip_longest(obj1.items(), obj2.items()):
        #print(key1, value1 + value2)
        if key1 in obj2_keys: # two matching keys were found
            del obj1_keys[key1]
            del obj2_keys[key1]



        if type(value1) != type(value2): # Type mismatches should return a tuple
            new_tuple = value1, value2
            new_obj[key1] = new_tuple

        else:
            if isinstance(value1, int) or isinstance(value1, (list,)) or isinstance(value1, str) or isinstance(value1, float ) : # integer, float, list, string
                new_val = value1 + value2
                new_obj[key1] = new_val
            elif isinstance(value1, set): # set
                new_set = value1.union(value2)
                new_obj[key1] = new_set
            elif isinstance(value1, dict): # recursive?
                pass


    print(new_obj)
    return new_obj



a = {'a': 1.2, 'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'a': 1.3, 'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}



#a = {'x': [1,2,3], 'y': 1, 'w': 'qweqwe', 'z': set([1,2,3]), 't': {'a': [1, 2]}}
#b = {'x': [4,5,6], 'y': 4, 'w': 'asdf', 'z': set([4,2,3]), 't': {'a': [3, 2]}}



merge_two_objects(a, b)



