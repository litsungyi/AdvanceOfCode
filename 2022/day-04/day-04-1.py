import re

PATTERN = r"(?P<start_1>[0-9]+)-(?P<end_1>[0-9]+),(?P<start_2>[0-9]+)-(?P<end_2>[0-9]+)"
count = 0
with open('./2022/day-04/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(PATTERN, line)
        start_1 = int(matches.group('start_1'))
        end_1 = int(matches.group('end_1'))
        start_2 = int(matches.group('start_2'))
        end_2 = int(matches.group('end_2'))

        if (start_1 >= start_2 and end_1 <= end_2) or \
           (start_2 >= start_1 and end_2 <= end_1):
            count += 1

    print(count)
