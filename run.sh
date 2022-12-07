#! /bin/bash

if [[ $# -ne 2 ]]
then
    echo "Usage ./run.sh {day-with-prefix-0} {part}"
    exit 1
fi

pyenv exec python "./2022/day-$1/day-$1-$2.py"
