import re

sum = 0
with open('./2023/day-02/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        game = line.split(":")
        game_index = int(re.findall(r"(\d+)", game[0])[0])
        colors = game[1].split(";")
        max_red = 0
        max_green = 0
        max_blue = 0
        for color_string in colors:
            r_matches = re.findall(r"(\d+) red", color_string)
            if len(r_matches) > 0:
                red = int(r_matches[0])
                max_red = max(max_red, red)
            g_matches = re.findall(r"(\d+) green", color_string)
            if len(g_matches) > 0:
                green = int(g_matches[0])
                max_green = max(max_green, green)
            b_matches = re.findall(r"(\d+) blue", color_string)
            if len(b_matches) > 0:
                blue = int(b_matches[0])
                max_blue = max(max_blue, blue)

        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            sum += game_index

print(sum)
