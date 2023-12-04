File = 'input.txt'
InputLen = 202

local function parse_count(inputline)
	local line, t = {}, {}
	for str in string.gmatch(inputline, "([^:|]+)") do table.insert(line, str) end
	local winning_nums, have_nums = line[2], line[3]
	for str in string.gmatch(winning_nums, "([^ ]+)") do t[str] = true end

	local value = 0
	for str in string.gmatch(have_nums, "([^ ]+)") do
		if t[str] then
			if value == 0 then value = 1 else value = value * 2 end
		end
	end
	return value
end

local function from_file(file)
	local lines = {}
	for line in io.lines(file) do lines[#lines + 1] = line end
	return lines
end

local function part_one(lines)
  local total = 0
  for i = 1, #lines do total = total + parse_count(lines[i]) end
	return total
end

print('Part 1 - total points: ' .. part_one(from_file(File)))

local function parse_cards(inputline, i, card_count)
	local line, t = {}, {}
	for str in string.gmatch(inputline, "([^:|]+)") do table.insert(line, str) end
	local winning_nums, have_nums = line[2], line[3]

	for str in string.gmatch(winning_nums, "([^ ]+)") do t[str] = true end

	local matches = 0
	for str in string.gmatch(have_nums, "([^ ]+)") do
		if t[str] then matches = matches + 1 end
	end

	-- Add additional cards
	for j = i + 1, i + matches do
		if j < InputLen then card_count[j] = card_count[j] + card_count[i] end
	end
end

local function part_two(lines)
  local card_count = {}
  for i = 1, #lines do card_count[i] = 1 end -- Set initial card counts to 1
  for i = 1, #lines do parse_cards(lines[i], i, card_count) end -- Add up all cards

	local total = 0
	for _, count in pairs(card_count) do total = total + count end
	return total
end

print('Part 2 - total cards: ' .. part_two(from_file(File)))
