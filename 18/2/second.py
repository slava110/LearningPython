import math


def main(z):
    if z < 59:
        return z**7 - 1
    if z < 89:
        return z**5/99 + math.sqrt(z)**3
    if z < 144:
        return 73 * z**5
    return 71 * z**2 + 31 * z**5
