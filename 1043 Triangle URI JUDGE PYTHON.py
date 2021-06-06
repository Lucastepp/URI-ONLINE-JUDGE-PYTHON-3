

A, B, C = map(float, input().split())

if (A + B <= C) or (A + C <= B) or (B + C <= A):
    area = ((A + B) * C) / 2
    print("Area = %.1f" %area)
else:
    perimetro = A + B + C
    print("Perimetro = %.1f" %perimetro)

