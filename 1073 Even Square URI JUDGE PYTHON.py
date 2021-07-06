var = int(input())

for i in range(1, var +1):
    if (i % 2 == 0):
        result = i ** 2
        print("{}^2 = {}".format(i, result))