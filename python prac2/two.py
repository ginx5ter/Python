import math

x = 1
y = 4
z = 3

c = math.fabs((math.cos(y) / math.sin(y)) + 6)

h = c ** (1. / 3.) + math.sqrt(math.pow((x + 1), 3)) / ((4 * y) - (2 * z))

print(h)
