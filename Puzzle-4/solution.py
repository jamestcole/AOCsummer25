# Read input
with open('input.txt', 'r') as file:
    datastream = file.read().strip()
    
def find_marker(datastream, marker_length):
    for i in range(marker_length, len(datastream) + 1):
        window = datastream[i - marker_length:i]
        if len(set(window)) == marker_length:
            return i
    return -1

# Part 1: Start-of-packet (4 unique chars)
part1 = find_marker(datastream, 4)
print(f"Part 1: {part1}")

# Part 2: Start-of-message (14 unique chars)
part2 = find_marker(datastream, 14)
print(f"Part 2: {part2}")
