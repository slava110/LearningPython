from math import *


def main(z):
    res = 0
    for i in range(0, len(z)):
        res += log(z[i]**3 + z[i] + 1)**2
    return 73 * res
