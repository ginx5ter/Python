from math import *


def area(choose):
    if choose == 'triangle':
        triangle()
    elif choose == 'rectangle':
        rectangle()
    elif choose == 'circle':
        circle()


def triangle():
    a = float(input('enter a: '))
    b = float(input('enter b: '))
    c = float(input('enter c: '))

    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)


def rectangle():
    a = float(input('enter a: '))
    b = float(input('enter b: '))

    s = a * b
    print(s)


def circle():
    r = float(input('enter r: '))

    s = pi * pow(r, 2)
    print(s)


choose = input('enter the shape: rectangle, triangle or circle   ')
area(choose)

