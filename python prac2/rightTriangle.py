from math import *


def perimetr(leg1, leg2, hypo):
    p = leg1 + leg2 + hypo
    return p


def area(a, b):
    s = (a * b) / 2
    return s


a = float(input('enter legs: '))
c = sqrt(pow(a, 2)+pow(a, 2))

print(perimetr(a, a, c))
print(area(a, a))
