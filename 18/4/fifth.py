import math


def main(n):
    match n:
        case 0:
            return -0.34
        case 1:
            return 0.33
        case _:
            return math.log(main(n - 1), 2) ** 2\
                + 1 + 53 * (main(n - 2) / 66 - 0.01)
