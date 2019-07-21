moves = input()

position = [1,0,0]

for i in range(len(moves)):
    if moves[i] == 'A':
       position[0], position[1] =  position[1], position[0]
    elif moves[i] == 'B':
       position[1], position[2] =  position[2], position[1]
    elif moves[i] == 'C':
       position[0], position[2] =  position[2], position[0]

print(position.index(1) + 1)