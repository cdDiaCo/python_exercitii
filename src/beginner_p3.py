
# open file

# read values from file into a data structure

# get the order of the dictionaries in the output file

# write output file




def get_dictionaries_list_from_file():

    lines_list = []
    with open('../dictionaries_list') as f:
        for line in f:
            lines_list.append(line.split())

    dict_list = [] # this will hold all the dictionaries from the input file
    dictionary = {} # this will hold the key-value pairs from the input file

    for elem in lines_list :
        if len(elem) > 0 : # line not empty
            key = elem[0]
            value = elem[1]
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

        key_i = get_lowest_key(dictionaries_list, i)

        for j in range(i + 1, len(dictionaries_list)):  # the remaining list to be sorted

            key_j = get_lowest_key(dictionaries_list, j)

            if dictionaries_list[min_pos][key_i] > dictionaries_list[j][key_j]:  # check which value is the lowest
                min_pos = j
                key_i = key_j

        switch_dictionaries(dictionaries_list, i, min_pos)
        switch_dictionaries(initial_pos_list, i, min_pos)
    print(initial_pos_list)


    return dictionaries_list



def get_lowest_key(list, element):
    sorted_keys_i = sorted(list[element].keys())  # get the key that has the min value for every dictionary in the first list
    key_i = sorted_keys_i[0]

    return key_i


def switch_dictionaries(list, prev_pos, new_pos):
    # switch the dictionary that has the new found lowest value with the dictionary in the first list

    temp = list[prev_pos]
    list[prev_pos] = list[new_pos]
    list[new_pos] = temp



def compare_dictionaries(previous_dict, current_dict, previous_key, current_key, current_pos, count) :

    if previous_dict[previous_key] > current_dict[current_key] :
        previous_dict = current_dict
        previous_key = current_key
        min_pos = current_pos

    elif previous_dict[previous_key] == current_dict[current_key] :
        count += 1








def write_output_file() :
    sorted_list = sort_list()
    print(sorted_list)

    with open("output_file", "w") as f:

        for elem in sorted_list :
            for key in elem :
                line = str(key) + " "
                f.write(line)
                #print(str(key))





write_output_file()





