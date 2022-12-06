CHARS = 'abcdefghijklmnopqrstuvwxyz'
with open('./2022/day-06/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        position = {char: -1 for char in CHARS}
        length = 0
        for index in range(0, len(line)):
            char = line[index]
            #print(f"char: {char}, index: {index}")
            if position[char] != -1:
                duplicate = position[char]
                #print(f"{char} duplicate at {duplicate}")
                for count in position:
                    if position[count] <= duplicate:
                        position[count] = -1

                length = index - duplicate
                #print(f"max: {max}, length: {length}")

            length += 1
            position[char] = index
            if length >= 14:
                print(index + 2)
                break
