import re

def to_index(node):
    return f"{node['x']}_{node['y']}"

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

def move_tail(direction, head, tail):
    x_distance = abs(head['x'] - tail['x'])
    y_distance = abs(head['y'] - tail['y'])
    distance = x_distance + y_distance
    # print(f"{head} -> {tail}, distance: {distance}, x_distance: {x_distance}, y_distance: {y_distance}")
    if distance <= 1:
        return [tail, distance]

    elif distance == 2 and x_distance != y_distance:
        if x_distance == 0:
            return [make_point(head['x'], head['y'] + sign(tail['y'] - head['y'])), distance]
        else:
            return [make_point(head['x'] + sign(tail['x'] - head['x']), head['y']), distance]

    elif distance >= 3:
        if x_distance > y_distance:
            return [make_point(head['x'] + sign(tail['x'] - head['x']), head['y']), distance]
        else:
            return [make_point(head['x'], head['y'] + sign(tail['y'] - head['y'])), distance]

    else:
        return [tail, distance]

PATTERN = '(?P<direction>[UDLR])\s(?P<count>[0-9]+)'
LENGTH = 9
nodes = [{'x': 0, 'y': 0} for i in range(LENGTH + 1)]

tail_index = to_index(nodes[LENGTH])
tails = {tail_index: True}
with open('./2022/day-09/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(PATTERN, line)
        if matches:
            direction = matches.group('direction')
            moves = int(matches.group('count'))

            for count in range(moves):
                nodes[0] = move_head(direction, nodes[0])
                for i in range(0, LENGTH):
                    prev = nodes[i + 1]
                    result = move_tail(direction, nodes[i], nodes[i + 1])
                    nodes[i + 1] = result[0]

                    if i == LENGTH - 1:
                        tail = nodes[LENGTH]
                        while prev['x'] != tail['x'] or prev['y'] != tail['y']:
                            tail_index = to_index(tail)
                            if not tail_index in tails:
                                tails[tail_index] = True

                            result = move_tail(direction, tail, prev)
                            tail = result[0]

print(len(tails))

# > 2563
# > 2552
# 2688 ?