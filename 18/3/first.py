import math


def main(b, y, m):
    q = 0
    for i in range(1, b + 1):
        q += i + 22 * (1 + i**3 / 14 + 73 * y)**2
    e = 0
    for c in range(1, m + 1):
        e += c**3 + 12*c**6 + math.ceil(c)**7/21
    return q - e
