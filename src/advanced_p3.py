

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    pass



obj_one = SingletonClass()
obj_two = SingletonClass()


if obj_one is obj_two:
    print("same object")
else:
    print("different objects")

