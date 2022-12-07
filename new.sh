#! /bin/bash

if [[ $# -ne 1 ]]
then
    echo "Usage ./new.sh {day-with-prefix-0}"
    exit 1
fi

YEAR=2022
DAY="$1"

if [[ ! -d "${YEAR}/day-${DAY}" ]]
then
    mkdir "${YEAR}/day-${DAY}"
fi

if [[ ! -e "${YEAR}/day-${DAY}/day-${DAY}-1.py" ]]
then
    echo "" >> "${YEAR}/day-${DAY}/day-${DAY}-1.py"
fi

if [[ ! -e "${YEAR}/day-${DAY}/day-${DAY}-2.py" ]]
then
    echo "" >> "${YEAR}/day-${DAY}/day-${DAY}-2.py"
fi
