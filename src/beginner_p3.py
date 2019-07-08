
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

        sorted_keys_i = sorted(dictionaries_list[i][initial_pos_i].keys())  # get the key that has the min value for every dictionary in the first list
        key_i = sorted_keys_i[count]

        for j in range(i + 1, len(dictionaries_list)):  # the remaining list to be sorted
            initial_pos_j = 0


            for key, value in dictionaries_list[j].items():
                initial_pos_j = key

            sorted_keys_j = sorted(dictionaries_list[j][initial_pos_j].keys())  # get the key that has the min value for every dictionary in the second list
            key_j = sorted_keys_j[count]


            #compare_dictionaries(min_dict, dictionaries_list[j][initial_pos_j], key_i, key_j)

            if min_dict[key_i] > dictionaries_list[j][initial_pos_j][key_j]:  # check which value is the lowest
                min_dict = dictionaries_list[j][initial_pos_j]
                key_i = key_j
                min_pos = j
                initial_pos_i = initial_pos_j


            elif min_dict[key_i] == dictionaries_list[j][initial_pos_j][key_j]:  # the two values are equal, reapply the algorithm ignoring the current key
                pass

                #count += 1

                #key_i = sorted_keys_i[count]
                #key_j = sorted_keys_j[count]




        # switch the dictionary that has the new found lowest value with the dictionary in the first list
        temp = dictionaries_list[min_pos]
        dictionaries_list[min_pos] = dictionaries_list[i]
        dictionaries_list[i] = temp

    return dictionaries_list



def compare_dictionaries() :
    pass



#print(sort_list())




def write_output_file() :
    sorted_list = sort_list()

    with open("output_file", "w") as f:

        for elem in sorted_list :
            for key in elem :
                line = str(key) + " "
                f.write(line)
                print(str(key))





write_output_file()





