CHARS = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_LENGTH = len(CHARS)
GROUP_SIZE = 3
scores = {}
for index in range(0, MAX_LENGTH):
    char = CHARS[index]
    scores[char] = index

data_index = 0
sum = 0
datas = []
with open('./2022/day-03/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        indeies = [0] * MAX_LENGTH
        for index in range(0, len(line)):
            char_index = scores[line[index]]
            indeies[char_index] = 1

        datas.append(indeies)
        data_index += 1
        if data_index == GROUP_SIZE:
            for index in range(0, MAX_LENGTH):
                if datas[0][index] == 1 and datas[1][index] == 1 and datas[2][index] == 1:
                    sum += index

            data_index = 0
            datas = []

    print(sum)
