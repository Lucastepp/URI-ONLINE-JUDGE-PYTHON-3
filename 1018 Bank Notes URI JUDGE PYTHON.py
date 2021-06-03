


import math

N = int(input())

cem = N / 100
resCem = math.floor(cem)
som1 = math.floor(cem) * 100

cinquenta = (N - math.floor(som1)) / 50
resCinquenta = math.floor(cinquenta)
som2 = math.floor(cinquenta) * 50

vinte = (N - math.floor(som1) - math.floor(som2)) / 20
resVinte = math.floor(vinte)
som3 = math.floor(vinte) * 20

dez = (N - math.floor(som1) - math.floor(som2) - math.floor(som3)) / 10
resDez = math.floor(dez)
som4 = math.floor(dez) * 10

cinco = (N - math.floor(som1) - math.floor(som2) - math.floor(som3) - math.floor(som4)) / 5
resCinco = math.floor(cinco)
som5 = math.floor(cinco) * 5

dois = (N - math.floor(som1) - math.floor(som2) - math.floor(som3) - math.floor(som4) - math.floor(som5)) / 2
resDois = math.floor(dois)
som6 = math.floor(dois) * 2

um = (N - math.floor(som1) - math.floor(som2) - math.floor(som3) - math.floor(som4) - math.floor(som5) - math.floor(som6)) / 1
resUm= math.floor(um)
som7 = math.floor(um) * 1

print(N)
print(resCem, "nota(s) de R$ 100,00")
print(resCinquenta, "nota(s) de R$ 50,00")
print(resVinte, "nota(s) de R$ 20,00")
print(resDez, "nota(s) de R$ 10,00")
print(resCinco, "nota(s) de R$ 5,00")
print(resDois, "nota(s) de R$ 2,00")
print(resUm, "nota(s) de R$ 1,00")
