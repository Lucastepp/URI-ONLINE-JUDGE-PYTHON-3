var = int(input())
counter_in = 0
counter_out = 0

for i in range(0, var):
    i = int(input())
    if (i >= 10 and i <= 20):
        counter_in += 1
    else:
        counter_out += 1
    if (i < 0):
        counter_out -= 1
print("{} in".format(counter_in))
print("{} out".format(counter_out))