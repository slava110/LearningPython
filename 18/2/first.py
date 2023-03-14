import math


def main(z):
    if z < 59:
        return z**7 - 1
    elif z < 89:
        return z**5/99 + math.sqrt(z)**3
    elif z < 144:
        return 73 * z**5
    else:
        return 71 * z**2 + 31 * z**5
