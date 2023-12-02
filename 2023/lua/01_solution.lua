File = 'input.txt'
Map = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}

function string.starts(String,Start)
  return string.sub(String,1,string.len(Start))==Start
end

local function from_file(file)
  local lines = {}
  for line in io.lines(file) do
  lines[#lines + 1] = line
  end
  return lines
end

local function part_one(lines)
  local sum = 0
  for _, line in pairs(lines) do
  local a, b
  for i = 1, #line do
    a = line:sub(i,i)
    if tonumber(a) then
    break
    end
  end

  for i = #line, 1, -1 do
    b = line:sub(i,i)
    if tonumber(b) then
    break
    end
  end

  sum = sum + tonumber(a .. b)
  end
  return sum
end

print('Part 1 - calibration values: ' .. part_one(from_file(File)))

local function search_map(remainder)
  for i, word in pairs(Map) do
  if string.starts(remainder, word) then
    return i
  end
  end
  return false
end

local function part_two(lines)
  local sum = 0
  for _, line in pairs(lines) do
  local a, b
  for i = 1, #line do
    a = line:sub(i,i)
    if tonumber(a) then
    break
    elseif search_map(line:sub(i, #line)) then
    a = search_map(line:sub(i, #line))
    break
    end
  end

  for i = #line, 1, -1 do
    b = line:sub(i,i)
    if tonumber(b) then
    break
    elseif search_map(line:sub(i, #line)) then
    b = search_map(line:sub(i, #line))
    break
    end
  end

  sum = sum + tonumber(a .. b)
  end
  return sum
end

print('Part 2 - calibration values: ' .. part_two(from_file(File)))
