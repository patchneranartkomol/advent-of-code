local function from_file(file)
  local lines = {}
  for line in io.lines(file) do
	lines[#lines + 1] = line
  end
  return lines
end

local file = 'input.txt'
local lines = from_file(file)
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

print('Part 1 - calibration values: ' .. sum)
