import random
import numpy as np


def func(x):
    return x+2


def monteCarlo(function, a, b, n):
    result = 0
    for i in range(n):
        result += func(random.uniform(a, b))
    return (result/n) * (b - a)


print(monteCarlo(func, 1, 4, 100000))