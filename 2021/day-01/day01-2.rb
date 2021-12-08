count = 0
previous = []
File.foreach('input.txt') { |line|
    previous.append( line.to_i )
    next if previous.length <= 3

    count += 1 if previous[3] > previous[0]
    previous.shift
}

puts count
