# Read input data
with open("day_3/input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def is_symbol(symbol: str) -> bool:
    return not symbol.isdigit() and symbol != '.'


part_numbers = []

for i, line in enumerate(lines):
    current_number = ''
    is_part_number = False
    for j, character in enumerate(line):
        if lines[i][j].isdigit():
            current_number += lines[i][j]
            # check left
            if j > 0 and is_symbol(lines[i][j-1]):
                is_part_number = True
            # check right
            if j < len(line) - 1 and is_symbol(lines[i][j+1]):
                is_part_number = True  
            # check up
            if i > 0 and is_symbol(lines[i-1][j]):
                is_part_number = True
            # check down
            if i < len(lines) - 1 and is_symbol(lines[i+1][j]):
                is_part_number = True
            # check top left
            if i > 0 and j > 0 and is_symbol(lines[i-1][j-1]):
                is_part_number = True
            # check top right 
            if i > 0 and j < len(line) - 1 and is_symbol(lines[i-1][j+1]):
                is_part_number = True
            # check bottom left
            if i < len(lines) - 1 and j > 0 and is_symbol(lines[i+1][j-1]):
                is_part_number = True
            # check bottom right
            if i < len(lines) - 1 and j < len(line) - 1 and is_symbol(lines[i+1][j+1]):
                is_part_number = True
            
            # check if we reach the number's end
            if j < len(line) - 1 and not lines[i][j+1].isdigit():
                if (is_part_number):
                    part_numbers.append(current_number)
                current_number = ''
                is_part_number = False
    if (is_part_number):
        part_numbers.append(current_number)

print(f"Part 1: answer is: {sum([int(number) for number in part_numbers])}")


def get_distinct_numbers_in_symbol_neighborhood(grid: list[str], i: int, j: int) -> list[tuple[int, int]]:
    neighbor_coordinates = []
    # For center line
    if j > 0 and grid[i][j-1].isdigit():
        neighbor_coordinates.append((i, j-1))
    if j < len(grid[i]) - 1 and grid[i][j+1].isdigit():
        neighbor_coordinates.append((i, j+1))

    # For top line
    if i > 0:
        digit_found = False
        for offset in [-1,0,1]:
            if grid[i-1][j+offset].isdigit() and not digit_found:
                neighbor_coordinates.append((i-1, j+offset))
                digit_found = True
            elif not grid[i-1][j+offset].isdigit():
                digit_found = False
    
    # For bottom line
    if i < len(grid) - 1:
        digit_found = False
        for offset in [-1,0,1]:
            if grid[i+1][j+offset].isdigit() and not digit_found:
                neighbor_coordinates.append((i+1, j+offset))
                digit_found = True
            elif not grid[i+1][j+offset].isdigit():
                digit_found = False
                
    return neighbor_coordinates

def get_full_number(grid: list[str], i: int, j: int) -> str:
    right_index = j
    left_index = j
    number = grid[i][j]
    while right_index < len(grid[i]) - 1 and grid[i][right_index+1].isdigit():
        number += grid[i][right_index+1]
        right_index += 1
    while left_index > 0 and grid[i][left_index-1].isdigit():
        number = grid[i][left_index-1] + number
        left_index -= 1
    return number


ratio_parts = []

for i, line in enumerate(lines):
    nearby_numbers = 0
    for j, character in enumerate(line):
        if lines[i][j]=='*':
            neighbors = get_distinct_numbers_in_symbol_neighborhood(lines, i, j)
            if len(neighbors) == 2:
                ratio_parts.append((get_full_number(lines, neighbors[0][0], neighbors[0][1]), get_full_number(lines, neighbors[1][0], neighbors[1][1])))

ratios = [int(ratio[0]) * int(ratio[1]) for ratio in ratio_parts]
print(f"Part 2: answer is: {sum(ratios)}")           