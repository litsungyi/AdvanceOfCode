#! /bin/bash

if [[ $# -ne 2 ]]
then
    echo "Usage ./run.sh {day-with-prefix-0} {part}"
    exit 1
fi

YEAR=2022
DAY="$1"
PART="$2"

pyenv exec python "./${YEAR}/day-${DAY}/day-${DAY}-${PART}.py"
