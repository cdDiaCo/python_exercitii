

def compare_dictionaries(first_dict, second_dict, count = 0):
    sorted_keys_first_dict = get_sorted_keys(first_dict)
    sorted_keys_second_dict = get_sorted_keys(second_dict)


    if first_dict[sorted_keys_first_dict[count]] > second_dict[sorted_keys_second_dict[count]] :
        print("true")
        return True
    elif first_dict[sorted_keys_first_dict[count]] == second_dict[sorted_keys_second_dict[count]] :
        print("equality")
        count += 1
        return compare_dictionaries(first_dict, second_dict, count)
    else :
        print("false")
        return False



def get_sorted_keys(dict):
    sorted_keys = sorted(dict.keys())  # get the key that has the min value for every dictionary in the first list

    return sorted_keys


