horizontal_position = 0
depth = 0

File.foreach('input.txt') { |line|
    m = line.match(/([a-z]*)\s([0-9]*)/)
    direction = m[1]
    value = m[2].to_i
    horizontal_position += value if direction == 'forward'
    depth -= value if direction == 'up'
    depth += value if direction == 'down'
}

puts horizontal_position * depth
