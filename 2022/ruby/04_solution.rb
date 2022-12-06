# frozen_string_literal: true

def fully_contains(a_start, b_start, a_end, b_end)
  a_start >= b_start && a_end <= b_end || \
    b_start >= a_start && b_end <= a_end
end

def overlaps(a_start, b_start, a_end, b_end)
  a_end < b_start || b_end < a_start
end

if __FILE__ == $PROGRAM_NAME
  lines = IO.readlines('../input/04_input.txt', chomp: true)
  total1 = total2 = 0
  lines.each do |line|
    a, b = line.split(',')
    a_spl = a.split('-')
    b_spl = b.split('-')
    a_start = a_spl[0].to_i
    a_end = a_spl[-1].to_i
    b_start = b_spl[0].to_i
    b_end = b_spl[-1].to_i
    total1 += fully_contains(a_start, b_start, a_end, b_end) ? 1 : 0
    total2 += overlaps(a_start, b_start, a_end, b_end) ? 1 : 0
  end
  puts "Part 1 - Fully contained: #{total1}"
  puts "Part 2 - Overlapping: #{total2}"
end
