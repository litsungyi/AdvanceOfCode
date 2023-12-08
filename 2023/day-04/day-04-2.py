import re
from functools import reduce

count = 10
datas = [{
    'card': 0,
    'rewards': 0,
    'amount': 0
}]
with open('./2023/day-04/input.txt', 'r') as input:
    index = 0
    for line in input:
        index += 1
        m = re.findall("\d+\s", line)
        numbers = [int(i) for i in m]
        rewards = [i for i in numbers[0:count] if i in numbers[count:]]

        data = {
            'card': index,
            'rewards': len(rewards),
            'amount': 1
        }
        datas.append(data)

for data in datas:
    if data['rewards'] > 0:
        start_index = data['card'] + 1
        end_index = start_index + data['rewards']
        for new_data in datas[start_index:end_index]:
            new_data['amount'] += data['amount']
            datas[new_data['card']] = new_data

sum = reduce(lambda sum, data : sum + data['amount'], datas, 0)
print(sum)
