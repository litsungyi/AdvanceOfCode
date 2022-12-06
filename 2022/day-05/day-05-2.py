import re

datas = [
    ["R", "G", "J", "B", "T", "V", "Z"], # 1
    ["J", "R", "V", "L"], #2
    ["S", "Q", "F"], #3
    ["Z", "H", "N", "L", "F", "V", "Q", "G"], #4
    ["R", "Q", "T", "J", "C", "S", "M", "W"], #5
    ["S", "W", "T", "C", "H", "F"], #6
    ["D", "Z", "C", "V", "F", "N", "J"], #7
    ["L", "G", "Z", "D", "W", "R", "F", "Q"], #8
    ["J", "B", "W", "V", "P"], #9
]

# datas = [
#     ["Z", "N"], #1
#     ["M", "C", "D"], #2
#     ["P"], #3
# ]

PATTERN = r"move (?P<times>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)"
with open('./2022/day-05/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(PATTERN, line)
        times = -int(matches.group('times'))
        move_from = int(matches.group('from')) - 1
        move_to = int(matches.group('to')) - 1

        datas[move_to] = datas[move_to] + datas[move_from][times:]
        datas[move_from] =  datas[move_from][:times]

    result = ''
    for index in range(len(datas)):
        result += datas[index][-1]

    print(result)
