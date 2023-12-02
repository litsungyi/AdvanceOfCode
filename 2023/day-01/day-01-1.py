import re

pattern_front = r"^[a-z]*([0-9])"
pattern_end = r"([0-9])[a-z]*$"
prog_front = re.compile(pattern_front)
prog_end = re.compile(pattern_end)
sum = 0

with open('./2023/day-01/test.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        m = re.findall("\d", line)
        value = int(m[0]) * 10 + int(m[-1])
        sum += value

print(sum)