

start, end = map(int, input().split())

if (start >= end):
    resultado = (24 - start) + end
else:
    resultado = end - start




print("O JOGO DUROU %.0f HORA(S)" %resultado)