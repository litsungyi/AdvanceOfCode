horizontal_position = 0
depth = 0
aim = 0

File.foreach('input.txt') { |line|
    m = line.match(/([a-z]*)\s([0-9]*)/)
    direction = m[1]
    value = m[2].to_i
    if direction == 'forward'
        horizontal_position += value
        depth += aim * value
    end
    aim -= value if direction == 'up'
    aim += value if direction == 'down'
}

puts horizontal_position * depth
