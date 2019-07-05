
# open file

# read values from file into a data structure

# get the order of the dictionaries in the output file

# write comments for sort_list function

#  write output file


def get_dictionaries_list_from_file():

    f = open('../dictionaries_list', 'r')
    lines_list = []
    for line in f:
        lines_list.append(line.split())
    f.close()

    dict_list = [] # this will hold all the dictionaries from the input file

    inner_dict = {} # this will hold the key-value pairs from the input file
    outer_dict = {} # this will hold the inner_dict and its initial position in the input file

    count = 1 # dict position in the input file
    for elem in lines_list :
        if len(elem) > 0 : # line not empty
            key = elem[0]
            value = elem[1]
            inner_dict[key] = value

        else : # empty line:  1. either the line that separates two dictionaries  2. or just empty line at the beginning or at the end of input file

            if len(inner_dict) > 0 : # this is the empty line that separates two dictionaries
                outer_dict[count] = inner_dict
                dict_list.append(outer_dict)

                inner_dict = {}
                outer_dict = {}

                count += 1

    return dict_list





def sort_list() :

    dictionaries_list = get_dictionaries_list_from_file()

    for i in range(len(dictionaries_list)) :
        min_dict = {}
        initial_pos_i = 0
        min_pos = i

        for key, value in dictionaries_list[i].items() :
            min_dict = value
            initial_pos_i = key

        sorted_keys_i = sorted(dictionaries_list[i][initial_pos_i].keys())
        key_i = sorted_keys_i[0]

        for j in range(i+1, len(dictionaries_list)) :
            initial_pos_j = 0

            for key, value in dictionaries_list[j].items():
                initial_pos_j = key

            sorted_keys_j = sorted(dictionaries_list[j][initial_pos_j].keys())
            key_j = sorted_keys_j[0]

            if min_dict[key_i] > dictionaries_list[j][initial_pos_j][key_j] :
                min_dict = dictionaries_list[j][initial_pos_j]
                key_i = key_j
                min_pos = j
                initial_pos_i = initial_pos_j

        temp = dictionaries_list[min_pos]
        dictionaries_list[min_pos] = dictionaries_list[i]
        dictionaries_list[i] = temp

    return dictionaries_list



print(sort_list())



def write_output_file() :
    pass




