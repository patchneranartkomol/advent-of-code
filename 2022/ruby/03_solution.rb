# frozen_string_literal: true

require 'set'

class Set
  def pop
    el = to_a.sample
    delete(el)
    el
  end
end

def rucksack_duplicate(line)
  n = line.length
  first = Set.new(line[0, n / 2].chars)
  second = Set.new(line[n / 2, n].chars)
  (first & second).pop
end

def group_duplicate(line1, line2, line3)
  first = Set.new(line1.chars)
  second = Set.new(line2.chars)
  third = Set.new(line3.chars)
  (first & second & third).pop
end

def get_priority(item)
  if item >= 'a'
    item.ord - 'a'.ord + 1
  else
    item.ord - 38
  end
end

if __FILE__ == $PROGRAM_NAME
  total1 = 0
  lines = IO.readlines('../input/03_input.txt', chomp: true)
  lines.each { |l| total1 += get_priority(rucksack_duplicate(l)) }
  puts "Part 1 - Sum of duplicate item priorities: #{total1}"
  total2 = 0
  (0...lines.length).step(3).each do |i|
    line1 = lines[i]
    line2 = lines[i + 1]
    line3 = lines[i + 2]
    total2 += get_priority(group_duplicate(line1, line2, line3))
  end
  puts "Part 2 - Sum of badge priorities: #{total2}"
end
