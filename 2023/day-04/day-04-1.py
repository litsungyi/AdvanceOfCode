import re

sum = 0
count = 10
with open('./2023/day-04/input.txt', 'r') as input:
    for line in input:
        m = re.findall("\d+\s", line)
        numbers = [int(i) for i in m]
        rewards = [i for i in numbers[0:count] if i in numbers[count:]]
        if len(rewards) > 0:
            sum += 2 ** (len(rewards) -1)

print(sum)
