import math


def main(z):
    res = 0
    for i in range(0, len(z)):
        res += math.log(z[i] ** 3 + z[i] + 1) ** 2
    return 73 * res
