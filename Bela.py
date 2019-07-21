hand = input().split()

dominant = hand[1]

values = {'A':[11,11],'K':[4,4],'Q':[3,3],'J':[20,2],'T':[10,10],'9':[14,0],'8':[0,0],'7':[0,0],}

sum = 0

for i in range(int(hand[0]) * 4):
    number = input()
    if number[1] == dominant:
        sum += values[number[0]][0]
    else:
        sum += values[number[0]][1]

print(sum)