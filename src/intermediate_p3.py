# importing libraries
import time
import math


def time_slow(threshold=0.05): # decorator factory

    def decorator(func) : # decorator

        def inner1(*args, **kwargs):
            # storing time before function execution
            begin = time.time()

            print(threshold)

            func(*args, **kwargs)

            # storing time after function execution
            end = time.time()

            print("Total time taken in : ", func.__name__, end - begin)

        return inner1
    return decorator


# without parameter
@time_slow()
def my_fast(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))



# with parameter
@time_slow(0.65)
def my_fast(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
my_fast(23)


