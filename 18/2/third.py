import math


def main(z):
    res = None
    if z < 59:
        res = z**7 - 1
    elif z < 89:
        res = z**5/99 + math.sqrt(z)**3
    elif z < 144:
        res = 73 * z**5
    else:
        res = 71 * z**2 + 31 * z**5

    return res
