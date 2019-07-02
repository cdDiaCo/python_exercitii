
def merge_two_objects(obj1, obj2):
    new_obj = {}
    obj1_keys_list = list(obj1)
    obj2_keys_list = list(obj2)
    print(obj1_keys_list)

    for key in obj1_keys_list :
        if key in obj2_keys_list:
            obj1_value = obj1[key]
            obj2_value = obj2[key]
            if type(obj1_value) != type(obj2_value):  # Type mismatches should return a tuple
                new_tuple = obj1_value, obj2_value
                new_obj[key] = new_tuple
            else:
                if isinstance(obj1_value, int) or isinstance(obj1_value, (list,)) or isinstance(obj1_value, str) or isinstance(obj1_value, float):  # integer, float, list, string
                    new_val = obj1_value + obj2_value
                    new_obj[key] = new_val
                    #print(new_obj[key])
                elif isinstance(obj1_value, set):  # set
                    new_set = obj1_value.union(obj2_value)
                    new_obj[key] = new_set
                elif isinstance(obj1_value, dict):  # recursive?
                    temp_obj = merge_two_objects(obj1_value, obj2_value)
                    new_obj[key] = temp_obj

            obj2_keys_list.remove(key)
        else:
            # this key from obj1 has no match in obj2
            new_obj = add_without_merging(key, obj1, new_obj)

    if len(obj2_keys_list) > 0:
        # some keys from obj2 do not have a match in obj1
        # and will be added without merging
        for key in obj2_keys_list:
            new_obj = add_without_merging(key, obj2, new_obj)

    print(new_obj)
    return new_obj



def add_without_merging(key, old_obj, new_obj):
    new_obj[key] = old_obj[key]
    return new_obj



a = {'a': 1.2, 'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2], 'b': 'ddd'}}
b = {'a': 1.3, 'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2], 'b': 'eee'}, 'm': "wer"}


#a = {'x': [1,2,3], 'y': 1}
#b = {'x': [4,5,6], 'y': 4}


merge_two_objects(a, b)



