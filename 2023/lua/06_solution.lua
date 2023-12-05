File = 'input.txt'

local function check_beats(time, hold_time, distance)
	local travel_time = time - hold_time
	return (travel_time * hold_time) > distance
end

local function from_file(file)
	local lines = {}
	for line in io.lines(file) do lines[#lines + 1] = line end
	return lines
end

local function part_one(lines)
	local times, distances = {}, {}
	for str in string.gmatch(lines[1], "([^ ]+)") do
		if tonumber(str) then table.insert(times, tonumber(str)) end
	end
	for str in string.gmatch(lines[2], "([^ ]+)") do
		if tonumber(str) then table.insert(distances, tonumber(str)) end
	end

	local product = 1
	for i = 1, #times do
		local count = 0
		for j = 1, times[i] - 1 do
			if check_beats(times[i], j, distances[i]) then count = count + 1 end
		end
		product = product * count
	end

	return product
end

print('Part 1 - product: ' .. part_one(from_file(File)))

local function part_two(lines)
	local times, distances = {}, {}
	for str in string.gmatch(lines[1], "([^ ]+)") do
		if tonumber(str) then table.insert(times, str) end
	end
	for str in string.gmatch(lines[2], "([^ ]+)") do
		if tonumber(str) then table.insert(distances, str) end
	end
	local race_time = tonumber(table.concat(times, ''))
	local race_dist = tonumber(table.concat(distances, ''))
	local min_hold, max_hold = 9007199254740992, 0
	for i = 1, race_time - 1 do
		if check_beats(race_time, i, race_dist) then
			min_hold = i
			break
		end
	end
	for i = race_time - 1, 1, -1 do
		if check_beats(race_time, i, race_dist) then
			max_hold = i
			break
		end
	end
	return max_hold - min_hold + 1
end

print('Part 2 - ways to beat: ' .. part_two(from_file(File)))
