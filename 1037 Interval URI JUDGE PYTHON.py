

var = float(input())

if (var >= 0) and (var <= 25.00):
    print("Intervalo (0,25]")

elif (var >= 25.01) and (var <= 50.00):
    print("Intervalo (25,50]")

elif (var >= 50.01) and (var <= 75.00):
    print("Intervalo (50,75]")

elif (var >= 75.01) and (var <= 100.00):
    print("Intervalo (50,75]")
    
else:
    print("Fora de intervalo")