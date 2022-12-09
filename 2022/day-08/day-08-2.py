datas = []
scenic_scores = []
with open('./2022/day-08/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        data = []
        scenic_score = []
        for char in line:
            data.append(int(char))
            scenic_score.append(1)
        datas.append(data)
        scenic_scores.append(scenic_score)

max_x = len(datas)
max_y = len(datas[0])
x_index = [x for x in range(max_x)]
y_index = [y for y in range(max_y)]

def get_scenic_score(height, indexs):
    scenic_score = 0
    for index in indexs:
        x = index[0]
        y = index[1]
        if datas[x][y] < height:
            scenic_score += 1
        else:
            scenic_score += 1
            break

    return scenic_score

def get_indexs(x, y):
    if type(y) is int:
        for x_index in x:
            yield (x_index, y)

    if type(x) is int:
        for y_index in y:
            yield (x, y_index)

max_scenic_score = 0
for x in x_index:
    for y in y_index:
        height = datas[x][y]
        scenic_score = get_scenic_score(height, get_indexs(x, range(y-1, -1, -1))) \
          * get_scenic_score(height, get_indexs(x, range(y+1, max_y))) \
          * get_scenic_score(height, get_indexs(range(x-1, -1, -1), y)) \
          * get_scenic_score(height, get_indexs(range(x+1, max_x), y))
        scenic_scores[x][y] = scenic_score

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)