a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

counter_even = 0
counter_odd = 0
counter_positive = 0
counter_negative = 0

if (a % 2 == 0):
    counter_even += 1
if (a % 2 != 0):
    counter_odd += 1
if (a > 0):
    counter_positive += 1
if (a < 0):
    counter_negative += 1

if (b % 2 == 0):
    counter_even += 1
if (b % 2 != 0):
    counter_odd += 1
if (b > 0):
    counter_positive += 1
if (b < 0):
    counter_negative += 1

if (c % 2 == 0):
    counter_even += 1
if (c % 2 != 0):
    counter_odd += 1
if (c > 0):
    counter_positive += 1
if (c < 0):
    counter_negative += 1

if (d % 2 == 0):
    counter_even += 1
if (d % 2 != 0):
    counter_odd += 1
if (d > 0):
    counter_positive += 1
if (d < 0):
    counter_negative += 1

if (e % 2 == 0):
    counter_even += 1
if (e % 2 != 0):
    counter_odd += 1
if (e > 0):
    counter_positive += 1
if (e < 0):
    counter_negative += 1


print("{} valor(es) par(es)".format(counter_even))
print("{} valor(es) impar(es)".format(counter_odd))
print("{} valor(es) positivo(s)".format(counter_positive))
print("{} valor(es) negativo(s)".format(counter_negative))
