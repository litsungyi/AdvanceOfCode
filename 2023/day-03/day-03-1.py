def get_number(number_string):
    return int(number_string)

def parse_number(number_string):
    if number_string == "":
        return number_string
    
    parts["numbers"].append({
        "number": get_number(number_string),
        "length": len(number_string),
        "row": row,
        "column": column - len(number_string)
    })
    return ""

number_string = ""
parts = {
    "symbols": [],
    "numbers": []
}
with open('./2023/day-03/input.txt', 'r') as input:
    row = 0
    for line in [line.strip('\n') for line in input]:
        column = 0
        for char in line:
            if char == '.':
                number_string = parse_number(number_string)

            elif char in '0123456789':
                number_string += char

            else:
                number_string = parse_number(number_string)
                parts["symbols"].append({
                    "symbol": char,
                    "row": row,
                    "column": column
                })

            column += 1

        number_string = parse_number(number_string)
        row += 1

def is_adjacent(number, symbol):
    return (symbol["row"] >= number["row"] - 1 and symbol["row"] <= number["row"] + 1) and (symbol["column"] >= number["column"] - 1 and symbol["column"] <= number["column"] + number["length"])

sum = 0
for number in parts["numbers"]:
    for symbol in parts["symbols"]:
        if is_adjacent(number, symbol):
            sum += number["number"]
            break

print(sum)
