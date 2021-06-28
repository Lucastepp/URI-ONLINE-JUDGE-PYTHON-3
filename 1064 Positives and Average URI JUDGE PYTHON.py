a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


counter = 0
sum = 0

if (a > 0):
    sum = sum + a
    counter += 1
if (b > 0):
    sum = sum + b
    counter += 1
if (c > 0):
    sum = sum + c
    counter += 1
if (d > 0):
    sum = sum + d
    counter += 1
if (e > 0):
    sum = sum + e
    counter += 1
if (f > 0):
    sum = sum + f
    counter += 1

average = sum / counter

print("{} valores positivos".format(counter))
print("{:.1f}".format(average))