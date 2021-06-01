


import math

X1, Y1 = input().split(" ")
X2, Y2 = input().split(" ")

x1 = float(X1)
y1 = float(Y1)
x2 = float(X2)
y2 = float(Y2)

distance = math.pow(((x2 - x1)**2) + ((y2 - y1)**2), 1/2)

print("%.4f" %distance)
