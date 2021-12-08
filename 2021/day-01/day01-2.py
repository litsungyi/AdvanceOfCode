file = open('input.txt', 'r')
lines = file.readlines()
 
count = 0
index = 0
previous = []
for line in lines:
    current = int(line)
    previous.append(current)
    if len(previous) > 3:
        prev = previous[0]
        previous = previous[1:]

        if current > prev:
            count += 1

print("{}".format(count))
