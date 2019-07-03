
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


