


N = int(input())

hour = N // 3600
rest = N % 3600
minute = rest // 60
sec = rest % 60

print(str(hour)+":"+ str(minute)+":"+ str(sec))
