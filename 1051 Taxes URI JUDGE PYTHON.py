

var1 = float(input())

if (var1 <= 2000):
    print("Isento")

elif (var1 > 2000.00 and var1 <= 3000.00):
    rest = var1 - 2000
    result1 = rest * 0.08
    print("R$ %.2f" %result1)

elif (var1 > 3000.00 and var1 <= 4500.00):
    rest = var1 - 3000
    result1 = rest * 0.18
    resto = result1 + (1000.00 * 0.08)
    print("R$ %.2f" %resto)

else:
    rest = var1 - 4500.00
    result1 = rest * 0.28
    resto = result1 + (1000.00 * 0.08) + (1500.00 * 0.18)
    print("R$ %.2f" %resto)