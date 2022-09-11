import math


def first(h):
    x = float(2)
    y = float(4)

    h = math.pow(x, y * x), x + math.pow(math.pow(x, x), y) - math.pow(x, 4)


def second(h):
    x = float(1)
    y = float(4)
    z = float(3)

    c = math.fabs((math.cos(y) / math.sin(y)) + 6)

    h = c ** (1. / 3.) + math.sqrt(math.pow((x + 1), 3)) / (4 * y - 2 * z)

    return h


print(second(h))


