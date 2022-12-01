# frozen_string_literal: true

if __FILE__ == $PROGRAM_NAME
  counts = []
  curr = 0
  File.readlines('../input/01_input.txt').each do |line|
    if line == "\n"
      counts << curr
      curr = 0
    else
      curr += Integer(line)
    end
  end
  counts << curr

  # Sorting entire array, rather than using heap,
  # as I'm not aware of a heap class in Ruby STL
  counts.sort!
  puts "Part 1, top cals carried by any single elf: #{counts[-1]}"
  puts "Part 2, total cals for top 3 elves: #{counts.last(3).sum}"
end
