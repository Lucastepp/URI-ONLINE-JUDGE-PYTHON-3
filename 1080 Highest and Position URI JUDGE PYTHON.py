1080 

n = int(input())
x = 0

for i in range(1, 100):
    a = int(input())
    if (a > x):
        bigger = a
        position = i + 1
        x = a

print(bigger)
print(position)