import math

n = input().split(' ')

hypotenuse = math.sqrt(int(n[1])**2 + int(n[2])**2)

for i in range(int(n[0])):
    if float(input()) <= hypotenuse:
        print('DA')
    else: 
        print('NE')