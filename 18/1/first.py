import math


def a(y):
    return (63 * y ** 3 + 47 * y) ** 6 + math.sin(y) ** 7


def b(y):
    return y ** 5 + 57 * y ** 6


def c(y):
    return (y ** 3 + 93 * y) ** 3


def d(y):
    return y ** 5


def main(y):
    return a(y) / b(y) - c(y) / d(y)
