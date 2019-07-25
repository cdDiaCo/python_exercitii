

tt = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))



# use iterator
class MyIterator:
    def __init__(self, list):
        self.list = list
        self.index = 0
        self.my_iter = None


    def __iter__(self):
        return self


    def __next__(self):
        if self.my_iter:
            try:
                return next(self.my_iter)
            except StopIteration:
                self.my_iter = None
                return next(self)
        try:
            node = self.list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1

        if isinstance(node, tuple, ):
            self.my_iter = MyIterator(node)
            return next(self.my_iter)
        elif node is not None:
            return node
        else:
            return next(self)


    def __str__(self):
        return "Interator pentru {}".format(self.list)




def print_iterator_output_using_for(iterator):
    for node in iterator:
        print(node)


output_iterator = MyIterator(tt)

print_iterator_output_using_for(output_iterator)
#print([node for node in output_iterator])





# use generator
def my_generator(list):
    for el in list:
        if isinstance(el, tuple,):
            yield from my_generator(el)
        else:
            if el is not None:
                yield el


def print_generator_output(output):
    while True:
        try:
            node = next(output)
        except StopIteration:
            break
        else:
            print(node)


def print_generator_output_using_for(output):
    for node in output:
        print(node)


output_generator = my_generator(tt)

#print_generator_output(output_generator)
#print_generator_output_using_for(output_generator)
