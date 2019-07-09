
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
    count = 0

    for i in range(len(dictionaries_list)):  # this is considered the 'sorted list'
        min_dict = {}
        initial_pos_i = 0
        min_pos = i

        for key, value in dictionaries_list[i].items():
            min_dict = value
            initial_pos_i = key

        key_i = get_lowest_key(dictionaries_list, i, initial_pos_i, count)


        for j in range(i + 1, len(dictionaries_list)):  # the remaining list to be sorted
            initial_pos_j = 0


            for key, value in dictionaries_list[j].items():
                initial_pos_j = key

            key_j = get_lowest_key(dictionaries_list, j, initial_pos_j, count)


            #compare_dictionaries(min_dict, dictionaries_list[j][initial_pos_j], key_i, key_j, current_pos, count)

            if min_dict[key_i] > dictionaries_list[j][initial_pos_j][key_j]:  # check which value is the lowest
                min_dict = dictionaries_list[j][initial_pos_j]
                key_i = key_j
                min_pos = j
                #initial_pos_i = initial_pos_j


            elif min_dict[key_i] == dictionaries_list[j][initial_pos_j][key_j]:  # the two values are equal, reapply the algorithm ignoring the current key
                pass

                #count += 1



        switch_dictionaries(dictionaries_list, i, min_pos)

    return dictionaries_list



def get_lowest_key(list, element, element_key, count):
    sorted_keys_i = sorted(list[element][element_key].keys())  # get the key that has the min value for every dictionary in the first list
    key_i = sorted_keys_i[count]

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





#write_output_file()





