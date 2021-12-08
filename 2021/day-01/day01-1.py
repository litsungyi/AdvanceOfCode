file = open('input.txt', 'r')
lines = file.readlines()
 
count = 0
previous = -1
for line in lines:
    current = int(line)
    if previous != -1 and current > previous:
        count += 1
    
    previous = current

print("{}".format(count))

