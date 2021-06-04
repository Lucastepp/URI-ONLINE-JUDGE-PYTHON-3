
n1, n2, n3, n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)


media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)



if (media >= 7.0):
    print("Media: %.1f" %media)
    print("Aluno aprovado.")
elif (media <= 5.0):
     print("Media: %.1f" %media)
     print("Aluno reprovado.")
else:
     average = (media + n5) / 2
     print("Media: %.1f" %media)
     print("Aluno em exame.")
     print("Nota do exame: %.1f" %n5)
     if (average >= 5.0):
        print("Aluno aprovado.")
        print("Media final: %.1f" %average)
     else:
        print("Aluno reprovado.")
        print("Media final: %.1f" %average)