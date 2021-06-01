

A, B, C = input().split(" ")

a = float(A)
b = float(B)
c = float(C)
pi = 3.14159

TRIANGULO = (a * c) / 2
CIRCULO =  pi * c**2
TRAPEZIO = ((a + b) / 2) * c 
QUADRADO = b * b 
RETANGULO = a * b 

print("TRIANGULO: %.3f" %TRIANGULO)
print("CIRCULO: %.3f" %CIRCULO)
print("TRAPEZIO: %.3f" %TRAPEZIO)
print("QUADRADO: %.3f" %QUADRADO)
print("RETANGULO: %.3f" %RETANGULO)
