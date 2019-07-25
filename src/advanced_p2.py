import itertools


new_set = {1, 2, 3}


def my_generator(my_set):
    for i in range(len(my_set)+1):
        for comb in itertools.combinations(my_set, i):
            output = set()
            for el in comb:
                output.add(el)
            yield output



for subset in my_generator(new_set):
    print(subset)



