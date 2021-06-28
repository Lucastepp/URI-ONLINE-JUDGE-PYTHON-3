#INPUTS

dia_inicio = int(input().split()[1])

hora_inicio, minutos_inicio, segundos_inicio = map(int, input().split(" : "))

dia_final = int(input().split()[1])

horas_final, minutos_final, segundos_final = map(int, input().split(" : "))


#CONDITIONALS


dia_total = dia_final - dia_inicio



hora_total = horas_final - hora_inicio


if hora_total < 0:
    hora_total += 24
    dia_total -= 1

minuto_total = minutos_final - minutos_inicio

if minuto_total < 0:
    minuto_total += 60
    hora_total -= 1

segundo_total = segundos_final - segundos_inicio

if segundo_total < 0:
    segundo_total += 60
    minuto_total -= 1


print("%d dia(s)" %dia_total)
print("%d hora(s)" %hora_total)
print("%d minuto(s)" %minuto_total)
print("%d segundo(s)" %segundo_total)