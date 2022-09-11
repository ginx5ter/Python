import math

# task 1

a = float(input('enter a: '))
b = float(input('enter b: '))
h = float(input('enter h: '))

s = ((math.pow(a, 2) + b) * h) / (2 * (a - b) + 4)

print(s)

# task 2

x = float(input('enter x: '))
y = float(input('enter y: '))

h = math.sqrt(math.cos(2*y)+math.sin(4*y)+math.sqrt(math.pow(math.e, x)+math.pow(math.e, -x)))/(math.pow((math.pow(math.e, -x)+math.pow(math.e, x)), 3)*(math.pow((math.sin(4*y)+math.cos(2*y)-2), 2)))

print(h)

