
def merge_two_objects(obj1, obj2):
    new_obj = {}
    obj1_keys_list = list(obj1)
    obj2_keys_list = list(obj2)

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
                elif isinstance(obj1_value, set):  # set
                    new_set = obj1_value.union(obj2_value)
                    new_obj[key] = new_set
                elif isinstance(obj1_value, dict):  # recursive
                    temp_obj = merge_two_objects(obj1_value, obj2_value)
                    new_obj[key] = temp_obj

            obj2_keys_list.remove(key)
        else:
            # this key from obj1 has no match in obj2
            new_obj = add_elem_without_merging(key, obj1, new_obj)

    if len(obj2_keys_list) > 0:
        # some keys from obj2 do not have a match in obj1
        # and will be added without merging
        for key in obj2_keys_list:
            new_obj = add_elem_without_merging(key, obj2, new_obj)

    return new_obj


def add_elem_without_merging(key, old_obj, new_obj):
    new_obj[key] = old_obj[key]
    return new_obj
