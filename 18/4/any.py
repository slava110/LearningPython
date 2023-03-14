import math


def main(n):
    if n == 0:
        return -0.34
    if n == 1:
        return 0.33
    return math.log(main(n - 1), 2)**2 + 1 + 53*(main(n - 2)/66 - 0.01)
