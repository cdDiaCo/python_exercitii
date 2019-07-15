import math
from src.intermediate_p3 import time_slow


def test_without_parameter() :
    @time_slow()
    def my_fast(num):
        math.factorial(num)

    my_fast(900)



def test_with_parameter() :
    @time_slow(0.65)
    def my_fast(num):
        math.factorial(num)

    my_fast(900)


