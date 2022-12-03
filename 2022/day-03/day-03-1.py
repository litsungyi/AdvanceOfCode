CHARS = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_LENGTH = len(CHARS)
scores = {}
for index in range(0, MAX_LENGTH):
    char = CHARS[index]
    scores[char] = index

sum = 0
with open('./2022/day-03/input.txt', 'r') as input:
    for compartments in [line.strip('\n') for line in input]:
        size = int(len(compartments) / 2)
        first = compartments[:size]
        first_indeies = [0] * MAX_LENGTH
        second = compartments[-size:]
        second_indeies = [0] * MAX_LENGTH
        for index in range(0, size):
            first_index = scores[first[index]]
            first_indeies[first_index] = 1
            second_index = scores[second[index]]
            second_indeies[second_index] = 1

        for index in range(0, MAX_LENGTH):
            if first_indeies[index] == 1 and second_indeies[index] == 1:
                sum += index

    print(sum)
