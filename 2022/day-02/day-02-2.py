# A: Rock, B: Paper, C: Scissors, X: Rock (1), Y: Paper (2), Z: Scissors (3)
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win
MATCH = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

with open('./2022/day-02/input.txt', 'r') as input:
    sum = 0
    for key in [line.strip('\n') for line in input]:
        sum += MATCH[key]

    print(sum)
