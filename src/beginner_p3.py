
# open file

# read values from file into a data structure

# get the order of the dictionaries in the output file

# write output file




def get_dictionaries_list_from_file():

    lines_list = []
    with open('dictionaries_list') as f:
        for line in f:
            lines_list.append(line.split())

    dict_list = [] # this will hold all the dictionaries from the input file
    dictionary = {} # this will hold the key-value pairs from the input file

    for elem in lines_list :
        if len(elem) > 0 : # line not empty
            key = elem[0]
            value = int(elem[1])
            dictionary[key] = value

        else : # empty line:  1. either the line that separates two dictionaries  2. or just empty line at the beginning or at the end of input file

            if len(dictionary) > 0 : # this is the empty line that separates two dictionaries
                dict_list.append(dictionary)
                dictionary = {}

    return dict_list



def sort_list() : # implementation of selection sort algorithm

    dictionaries_list = get_dictionaries_list_from_file()
    initial_pos_list = list(range(len(dictionaries_list)))

    for i in range(len(dictionaries_list)):  # this is considered the 'sorted list'
        min_pos = i

        for j in range(i + 1, len(dictionaries_list)):  # the remaining list to be sorted
            res = is_smaller(dictionaries_list[min_pos], dictionaries_list[j])
            if res :
                min_pos = j

        switch_dictionaries(dictionaries_list, i, min_pos)
        switch_dictionaries(initial_pos_list, i, min_pos)

    print(initial_pos_list)
    print(dictionaries_list)

    return initial_pos_list



def get_sorted_keys(dict):
    sorted_keys = sorted(dict.keys())  # get the key that has the min value for every dictionary in the first list
    return sorted_keys



def switch_dictionaries(list, prev_pos, new_pos):
    # switch the dictionary that has the new found lowest value with the dictionary in the first list
    temp = list[prev_pos]
    list[prev_pos] = list[new_pos]
    list[new_pos] = temp



def is_smaller(first_dict, second_dict, count = 0): # check if second dictionary is smaller
    sorted_keys_first_dict = get_sorted_keys(first_dict)
    sorted_keys_second_dict = get_sorted_keys(second_dict)


    if count >= len(sorted_keys_first_dict) : # first dictionary is smaller because it has fewer elements
        return False
    elif count >= len(sorted_keys_second_dict) : # second dictionary is smaller because it has fewer elements
        return True


    if first_dict[sorted_keys_first_dict[count]] > second_dict[sorted_keys_second_dict[count]] : # the second dictionary is smaller
        return True
    elif first_dict[sorted_keys_first_dict[count]] == second_dict[sorted_keys_second_dict[count]] : # equal values, repeat with the next smallest keys
        count += 1
        return is_smaller(first_dict, second_dict, count)
    else : # the second dictionary is bigger
        return False



def write_output_file() :
    sorted_list = sort_list()

    with open("output_file", "w") as f:

        for pos in sorted_list :
            line = str(pos) + " "
            f.write(line)



write_output_file()





