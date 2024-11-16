import re

PATTERN = '(?P<op>addx|noop)(?P<value>\s?-?[0-9]+)?'
sum = 0
step = 0
x = 1
with open('./2022/day-10/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(PATTERN, line)
        if not matches:
            continue

        op = matches.group('op')
        if op == 'addx':
            step += 1
            if (step - 20) % 40 == 0:
                sum += x * step

            step += 1
            if (step - 20) % 40 == 0:
                sum += x * step

            x += int(matches.group('value'))
        else:
            step += 1
            if (step - 20) % 40 == 0:
                sum += x * step

print(sum)