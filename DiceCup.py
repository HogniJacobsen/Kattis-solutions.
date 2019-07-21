rolls = input().split()

sum_dict = dict()
max  = 0 

for i in range(1, int(rolls[0]) + 1):
    for j in range(1, int(rolls[1]) + 1):
        sum = i + j
        if sum not in sum_dict:
           sum_dict[sum] = 0
        else:
            sum_dict[sum] += 1
            if sum_dict[sum] > max:
                max = sum_dict[sum]

for i in sum_dict:
    if sum_dict[i] == max:
        print(i)