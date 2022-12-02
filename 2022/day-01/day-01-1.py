total = []
sum = 0
with open('./2022/day-01/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        if len(line) == 0:
            total.append(sum)
            sum = 0
        else:
            sum += int(line)

total.sort()
print(total[-1])
