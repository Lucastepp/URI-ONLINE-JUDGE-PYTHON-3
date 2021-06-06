

A, B = map(int, input().split())

if (A > B):
   ((A / B) % (A + B) == 0)
   print("Sao Multiplos")
elif (B > A):
   ((B / A) % (B + A) == 0)
   print("Sao Multiplos")
elif (A > B):
   ((A / B) % (A + B) != 0)
   print("Nao sao Multiplos")
elif (B > A):
   ((B / A) % (B + A) != 0)
   print("Nao sao Multiplos")
else:
   print("Nao sao Multiplos")