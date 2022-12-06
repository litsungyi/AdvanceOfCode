with open('./2022/day-06/input.txt', 'r') as input:
    input = input.readline()
    for index in range(0, len(input) - 3):
        if input[index] != input[index + 1] and \
            input[index] != input[index + 2] and \
            input[index] != input[index + 3] and \
            input[index + 1] != input[index + 2] and \
            input[index + 1] != input[index + 3] and \
            input[index + 2] != input[index + 3]:
            print(index + 4)
            break
