

def flatten(list_a, list_b, max_depth):
    if max_depth < 1:
        return list_a, list_b


    new_list_a = get_flat_list_recursive(list_a, max_depth)
    new_list_b = get_flat_list_recursive(list_b, max_depth)
    return new_list_a, new_list_b




def get_flat_list_recursive(old_list, max_depth):
    new_list = []
    for elem in old_list:
        if isinstance(elem,(list,)) and max_depth > 0 :
            # max_depth -= 1
            new_list.extend(get_flat_list_recursive(elem, max_depth-1))
        else:
            new_list.append(elem)


    return new_list

