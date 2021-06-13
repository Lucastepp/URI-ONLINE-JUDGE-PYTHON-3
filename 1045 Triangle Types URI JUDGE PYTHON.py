

A, B, C = map(float, input().split())

list = [ A, B, C ]
list = sorted(list, reverse=True)

if (A >= B + C):
    print("NAO FORMA TRIANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    elif ((A == B) and (B != C)) or ((A != B) and (B == C)) or ((A != B) and (B != C)):
        print("TRIANGULO ISOSCELES")

elif (A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    elif ((A == B) and (B != C)) or ((A != B) and (B == C)) or ((A != B) and (B != C)):
        print("TRIANGULO ISOSCELES")

elif (A**2 > B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    elif ((A == B) and (B != C)) or ((A != B) and (B == C)) or ((A != B) and (B != C)):
        print("TRIANGULO ISOSCELES")

elif (A**2 < B**2 + C**2):
    print("TRIANGULO ACUTANGULO")
    if (A == B == C):
        print("TRIANGULO EQUILATERO")
    elif ((A == B) and (B != C)) or ((A != B) and (B == C)) or ((A != B) and (B != C)):
        print("TRIANGULO ISOSCELES")