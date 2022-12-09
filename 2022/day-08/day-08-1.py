datas = []
visibles = []
with open('./2022/day-08/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        data = []
        visible = []
        for char in line:
            data.append(int(char))
            visible.append(False)
        datas.append(data)
        visibles.append(visible)

MAX_HEIGHT = 9
max_x = len(datas)
max_y = len(datas[0])
x_index = [x for x in range(max_x)]
y_index = [y for y in range(max_y)]

def check_height(x, y, height):
    current_height = datas[x][y]
    if current_height <= height:
        return height

    visibles[x][y] = True
    return current_height

for x in x_index[1:-1]:
    height = datas[x][0]
    visibles[x][0] = True
    for y in y_index[1:-1]:
        height = check_height(x, y, height)
        if height == MAX_HEIGHT:
            break

    height = datas[x][max_y - 1]
    visibles[x][max_y - 1] = True
    for y in y_index[-2:0:-1]:
        height = check_height(x, y, height)
        if height == MAX_HEIGHT:
            break

for y in y_index[1:-1]:
    height = datas[0][y]
    visibles[0][y] = True
    for x in x_index[1:-1]:
        height = check_height(x, y, height)
        if height == MAX_HEIGHT:
            break

    height = datas[max_x - 1][y]
    visibles[max_x - 1][y] = True
    for x in x_index[-2:0:-1]:
        height = check_height(x, y, height)
        if height == MAX_HEIGHT:
            break

total_visible = 4
for i in range(max_x):
    for j in range(max_y):
        if visibles[i][j]:
            total_visible += 1

print(total_visible)
