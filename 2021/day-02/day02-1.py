import re

file = open('input.txt', 'r')
lines = file.readlines()

horizontal_position = 0
depth = 0
for line in lines:
    m = re.match("([a-z]*)\s([0-9]*)", line)
    direction = m.groups()[0]
    value = int(m.groups()[1])
    if direction == 'forward':
        horizontal_position += value
    elif direction == 'up':
        depth -= value
    elif direction == 'down':
        depth += value

print(horizontal_position * depth)
