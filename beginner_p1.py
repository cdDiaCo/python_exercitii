

def flatten(list_a, list_b, max_depth):

    if max_depth > 0:
        new_list_a = []
        new_list_b = []

        get_flat_list_recursive(list_a, new_list_a, max_depth)
        get_flat_list_recursive(list_b, new_list_b, max_depth)
        return new_list_a, new_list_b

    return list_a, list_b



def get_flat_list_recursive(old_list, new_list, max_depth):

    for elem in old_list:
        if isinstance(elem,(list,)) and max_depth > 0 :
            max_depth -= 1
            get_flat_list_recursive(elem, new_list, max_depth)
        else:
            new_list.append(elem)



fruit_list = ['apple', ['cherry', 'banana', ['kiwi', 'mango'], 'strawberry', 'orange'], 'lemon']
numbers_list = [1, 2, [3, 4, 5, 6, 7], 8]
letters_list = []


a, b = flatten(fruit_list, numbers_list, 0)
print(a)
print(b)

