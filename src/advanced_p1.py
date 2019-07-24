

# use iterator
class MyIterator:
    def __init__(self, list):
        self.list = list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            node = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return node



def print_iterator_output(iterator):
    while True:
        try:
            node = next(iterator)
        except StopIteration:
            break
        else:
            if isinstance(node, tuple,):
                print_iterator_output(MyIterator(node))
            else:
                if node is not None:
                    print(node)


tt = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))

output_iterator = MyIterator(tt)

print_iterator_output(output_iterator)






# use generator
def my_generator(list):
    for el in list:
        if isinstance(el, tuple,):
            yield from my_generator(el)
        else:
            if el is not None:
                yield el


tt = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))

output_generator = my_generator(tt)


while True:
    try:
        node = next(output_generator)
    except StopIteration:
        break
    else:
        print(node)


