
# open file

# read values from file into a data structure

# get the order of the dictionaries in the output file

#  write output file


def get_dictionaries_list_from_file():

    f = open('../dictionaries_list', 'r')
    lines_list = []
    for line in f:
        lines_list.append(line.split())
    f.close()

    dict_list = [] # this will hold all the dictionaries from the input file

    new_dict = {}
    for elem in lines_list :
        if len(elem) > 0 : # line not empty
            key = elem[0]
            value = elem[1]
            new_dict[key] = value

            if elem == lines_list[-1] : # last elem in the list
                dict_list.append(new_dict)
                new_dict = {}

        else : # empty line:    1. either the line that separates two dictionaries  2. or just empty line at the beginning or at the end of input file

            if len(new_dict) > 0 : # this is the empty line that separates two dictionaries
                dict_list.append(new_dict)
                new_dict = {}

    return dict_list




#dictionaries_list = get_dictionaries_list_from_file()



dictionaries_list = get_dictionaries_list_from_file()
#print(dictionaries_list)

output_list = []

for i in range(len(dictionaries_list)) :
    min_dict = dictionaries_list[i]
    min_pos = i

    sorted_keys_i = sorted(dictionaries_list[i].keys())
    key_i = sorted_keys_i[0]

    for j in range(i+1, len(dictionaries_list)) :
        sorted_keys_j = sorted(dictionaries_list[j].keys())
        key_j = sorted_keys_j[0]
        #print(min_dict[key_i])
        #print(dictionaries_list[j][key_j])


        if min_dict[key_i] > dictionaries_list[j][key_j] :
            #print('true')
            min_dict = dictionaries_list[j]
            key_i = key_j
            min_pos = j

    print(min_pos)
    temp = min_dict
    dictionaries_list[min_pos] = dictionaries_list[i]
    dictionaries_list[i] = min_dict


    print(dictionaries_list)









# 3, 2, 5, 1, 4



'''

for i in range(len(dictionaries_list)) :
    print("outer for")
    sorted_keys_i = sorted(dictionaries_list[i].keys())
    key_i = sorted_keys_i[0]
    lowest_key_value_i = dictionaries_list[i][key_i]
    min_pos = dictionaries_list[i]

    for j in range(i + 1, len(dictionaries_list)):
        print("inner for")
        sorted_keys_j = sorted(dictionaries_list[j].keys())
        key_j = sorted_keys_j[0]
        #print(key_j)
        print(dictionaries_list[i])
        print(dictionaries_list[j])
        lowest_key_value_j = dictionaries_list[j][key_j]

        if lowest_key_value_i > lowest_key_value_j :
            print("true")
            # found a new minim
            lowest_key_value_i = lowest_key_value_j
            print(type(min_pos))
            min_pos = j
            print(lowest_key_value_i)


    temp = dictionaries_list[i]
    dictionaries_list[i] = dictionaries_list[min_pos]
    min_pos = temp  # nu se face schimbul in lista de dictionare
    print(dictionaries_list)


#print(dictionaries_list)


'''







#print(dictionaries_list)

# get the lowest alphabetic key for each dictionary -> if equality get the second lowest alphabetic key (recursive maybe?)

# compare the values of those keys

# get the output integers


