

var = int(input())

year = var // 365
rest = var % 365
month = rest // 30
day = var - ((year * 365) + (month * 30))


print(year, "ano(s)")
print(month, "mes(es)")
print(day, "dia(s)")