if [ "$#" -ne 2 ]; then
    echo "Usage ./run.sh {day} {part}"
    echo "  day: 01-25"
    echo "  part: 1-2"
    exit 1
fi

if [ ! -d "day-$1" ]; then
    echo "day-$1 not exist!"
    exit 2
fi


if [ -f "day-$1/day$1-$2.cpp" ]; then
    echo "cpp:"
    rm -f main.o
    docker run -it --rm \
        --name cpp-host \
        -v "$PWD"/day-$1:/usr/src/app \
        -w /usr/src/app \
        cpp-base \
        g++ -o main.o day$1-$2.cpp
    docker run -it --rm \
        --name cpp-host \
        -v "$PWD"/day-$1:/usr/src/app \
        -w /usr/src/app \
        cpp-base \
        ./main.o
    echo ""
else
    echo "day-$1/day$1-$2.cpp not found!"
fi

if [ -f "day-$1/day$1-$2.js" ]; then
    echo "node:"
    docker run -it --rm \
        --name node-host \
        -v "$PWD"/day-$1:/usr/src/app \
        -w /usr/src/app \
        node-base \
        node day$1-$2.js
    echo ""
else
    echo "day-$1/day$1-$2.js not found!"
fi

if [ -f "day-$1/day$1-$2.py" ]; then
    echo "python"
    docker run -it --rm \
        --name python-host \
        -v "$PWD"/day-$1:/usr/src/app \
        -w /usr/src/app \
        python-base \
        python day$1-$2.py
    echo ""
else
    echo "day-$1/day$1-$2.py not found!"
fi

if [ -f "day-$1/day$1-$2.rb" ]; then
    echo "ruby"
    docker run -it --rm \
        --name ruby-host \
        -v "$PWD"/day-$1:/usr/src/app \
        -w /usr/src/app \
        ruby-base \
        ruby day$1-$2.rb
    echo ""
else
    echo "day-$1/day$1-$2.rb not found!"
fi
