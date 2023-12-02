import re

def toNumber(key):
    number_string = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    if key in number_string:
        return number_string[key]
    else:
        return int(key)

with open('./2023/day-01/input.txt', 'r') as input:
    sum = 0
    for line in [line.strip('\n') for line in input]:
        m = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        value = toNumber(m[0]) * 10 + toNumber(m[-1])
        print(f"{line}: {m} => {m[0]}={toNumber(m[0])}, {m[-1]}={toNumber(m[-1])} = {value}")
        sum += value

    print(sum)
