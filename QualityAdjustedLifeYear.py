n = input()

qaly = 0

for i in range(int(n)):
    period = input().split()
    qaly = qaly + (float(period[0]) * float(period[1]))

print(qaly)