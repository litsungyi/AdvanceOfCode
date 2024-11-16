import re

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def make_point(x, y):
    return {'x': x, 'y': y}

def move_head(direction, head):
    match direction:
        case 'U':
            return make_point(head['x'], head['y'] - 1)

        case 'D':
            return make_point(head['x'], head['y'] + 1)

        case 'L':
            return make_point(head['x'] - 1, head['y'])

        case 'R':
            return make_point(head['x'] + 1, head['y'])

def move_tail(head, tail):
    x_distance = abs(head['x'] - tail['x'])
    y_distance = abs(head['y'] - tail['y'])
    distance = x_distance + y_distance
    if distance <= 1:
        return tail
    elif distance == 2 and x_distance != y_distance:
        if x_distance == 0:
            return make_point(head['x'], head['y'] + sign(tail['y'] - head['y']))
        else:
            return make_point(head['x'] + sign(tail['x'] - head['x']), head['y'])

    elif distance == 3:
        if x_distance > y_distance:
            return make_point(head['x'] + sign(tail['x'] - head['x']), head['y'])
        else:
            return make_point(head['x'], head['y'] + sign(tail['y'] - head['y']))

    else:
        return tail

PATTERN = '(?P<direction>[UDLR])\s(?P<count>[0-9]+)'
head = {'x': 0, 'y': 0}
tail = {'x': 0, 'y': 0}
tail_index = f"{tail['x']}_{tail['y']}"
tails = {tail_index: True}
with open('./2022/day-09/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(PATTERN, line)
        if matches:
            direction = matches.group('direction')
            moves = int(matches.group('count'))

            for count in range(moves):
                head = move_head(direction, head)
                tail = move_tail(head, tail)
                tail_index = f"{tail['x']}_{tail['y']}"
                if not tail_index in tails:
                    tails[tail_index] = True

print(len(tails))
