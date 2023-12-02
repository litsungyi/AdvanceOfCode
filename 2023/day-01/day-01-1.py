import re

with open('./2023/day-01/input.txt', 'r') as input:
    sum = 0
    for line in [line.strip('\n') for line in input]:
        m = re.findall("\d", line)
        value = int(m[0]) * 10 + int(m[-1])
        sum += value

    print(sum)
