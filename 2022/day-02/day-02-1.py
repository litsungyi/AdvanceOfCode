# A: Rock, B: Paper, C: Scissors, X: Rock (1), Y: Paper (2), Z: Scissors (3)
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
MATCH = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

with open('./2022/day-02/input.txt', 'r') as input:
    sum = 0
    for key in [line.strip('\n') for line in input]:
        sum += MATCH[key]

    print(sum)
