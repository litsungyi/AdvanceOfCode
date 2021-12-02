count = 0
prev = nil
File.foreach('input.txt') { |line| 
    count += 1 if prev.nil? || line.to_i > prev
    prev = line.to_i
}

puts count
