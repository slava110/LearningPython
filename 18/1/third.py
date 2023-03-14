from math import *


def main(y):
    a = ((63 * y ** 3 + 47 * y) ** 6 + sin(y) ** 7) / (y ** 5 + 57 * y ** 6)
    b = (y ** 3 + 93 * y) ** 3 / y ** 5
    return a - b
