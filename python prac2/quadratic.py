from math import *


def formula():
    try:
        a = float(input('enter a: '))
        b = float(input('enter b: '))
        c = float(input('enter c: '))
        d = sqrt(pow(b, 2) - 4 * a * c)

        if d > 0:
            x1 = (-b + d) / (2 * a)
            x2 = (-b - d) / (2 * a)
            print( x1, x2)
        elif d == 0:
            x1 = -b / (2 * a)
            print(x1)
    except ValueError:
        print('error')

formula()

