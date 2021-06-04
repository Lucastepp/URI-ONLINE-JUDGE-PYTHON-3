

import math

A, B, C= input().split(" ")

A = float(A)
B = float(B)
C = float(C)


if (A and B and C >= 0.00):
    X = (B**2)-(4*A*C)

    if (X <= 0):
         print("Impossivel calcular")

    else:
        X = math.sqrt(X)
        R1 = (-B+X)/(2*A)
        R2 = (-B-X)/(2*A)
    
        print("R1 = %.5f" %R1)
        print("R2 = %.5f" %R2)

else:
    print("Impossivel calcular")