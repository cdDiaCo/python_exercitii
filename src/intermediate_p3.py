# importing libraries
import time
import math


def time_slow(threshold=0.05): # decorator factory

    def decorator(func) : # decorator

        def inner1(*args, **kwargs):
            # storing time before function execution
            begin = time.time()

            func(*args, **kwargs)

            # storing time after function execution
            end = time.time()

            total_time = end-begin

            if total_time > threshold :
                print("Total time taken in : ", func.__name__, total_time)

        return inner1
    return decorator



'''
# without parameter
@time_slow()
def my_fast(num):
    math.factorial(num)


# with parameter
@time_slow(0.65)
def my_fast(num):
    math.factorial(num)


# calling the function,
my_fast(599900)

'''
