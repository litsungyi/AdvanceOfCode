import re

COMMAND_PATTERN = '^\$ (?P<command>cd|ls)\s?(?P<param>.*)?'
SIZE_PATTERN = '(?P<size>[0-9]+)\s(?P<name>.*)'
current_folder = []
size_data = {}

def chdir(folder):
    global current_folder
    if folder == '..':
        current_folder = current_folder[:-1]
    elif folder == '/':
        current_folder = ['']
    else:
        current_folder.append(folder)

with open('./2022/day-07/input.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        matches = re.search(COMMAND_PATTERN, line)
        if matches:
            command = matches.group('command')
            if command != 'cd':
                continue

            param = matches.group('param')
            chdir(param)
        else:
            path = '/'.join(current_folder)
            size_matches = re.search(SIZE_PATTERN, line)
            if not size_matches:
                dir = f"{path}/{line[4:]}"
                if path in size_data:
                    size_data[path]['dirs'].append(dir)
                else:
                    size_data[path] = {
                        "size": 0,
                        "dirs": [dir]
                    }
                continue

            size = int(size_matches.group('size'))

            if path in size_data:
                size_data[path]['size'] += size
            else:
                size_data[path] = {
                    "size": size,
                    "dirs": []
                }

def get_total_size(path):
    global size_data
    data = size_data[path]
    size = data['size']

    for folder in data['dirs']:
        size += get_total_size(folder)

    return size

total_size = 0
for path in size_data:
    size = get_total_size(path)
    if size <= 100000:
        total_size += size

print(total_size)
