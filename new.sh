#! /bin/bash

if [[ $# -ne 1 ]]
then
    echo "Usage ./new.sh {day-with-prefix-0}"
    exit 1
fi

YEAR=2023
DAY="$1"

mkdir -p "${YEAR}/day-${DAY}"

if [[ ! -e "${YEAR}/day-${DAY}/day-${DAY}-1.py" ]]
then
    echo "with open('./${YEAR}/day-${DAY}/test-1.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        pass" >> "${YEAR}/day-${DAY}/day-${DAY}-1.py"
fi

if [[ ! -e "${YEAR}/day-${DAY}/day-${DAY}-2.py" ]]
then
    echo "with open('./${YEAR}/day-${DAY}/test-2.txt', 'r') as input:
    for line in [line.strip('\n') for line in input]:
        pass" >> "${YEAR}/day-${DAY}/day-${DAY}-2.py"
fi

if [[ ! -e "${YEAR}/day-${DAY}/input.txt" ]]
then
    echo "" >> "${YEAR}/day-${DAY}/input.txt"
fi

if [[ ! -e "${YEAR}/day-${DAY}/test-1.txt" ]]
then
    echo "" >> "${YEAR}/day-${DAY}/test-1.txt"
fi

if [[ ! -e "${YEAR}/day-${DAY}/test-2.txt" ]]
then
    echo "" >> "${YEAR}/day-${DAY}/test-2.txt"
fi
