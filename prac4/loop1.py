#1st task

p = int(input('enter price: '))
q = int(input('enter quantity: '))
x = range(1, q + 1)
for i in x:
    print(i * p)


#2nd task

x = [10,20,30,40,50,60]

size = len(x)

# 2nd task b
i = 1
while i < size:
    i = i + 1
print(i)

# 2nd task a
sum = 0
j = 0
while j < size:
    sum+=x[j]
    j = j + 1
print(sum)

