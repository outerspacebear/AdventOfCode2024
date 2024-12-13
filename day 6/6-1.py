import re
from enum import Enum

class Direction(Enum):
    Up = 1
    Down = 2
    Left = 3
    Right = 4


def get_lines(input_file):

    lines = []

    for line in input_file:
        lines.append(line.split())

    return lines

def get_map_grid(lines):

    rows = []
    row_index = 0
    for line in lines:
        row = list(line)[0]
        #print(row[0])
        rows.append(row)

    #print(rows)
    return rows

def is_guard(character):

    if character == '^' or character == '<' or character == '>' or character == 'v':
        return True
    return False

def get_guard_position(map_grid):

    for row_index in range(0, len(map_grid)):
        for col_index in range(0, len(map_grid[row_index])):
            if is_guard(map_grid[row_index][col_index]):
                return row_index, col_index
            
    print("Error: Could not find guard!")
    return 0, 0

def is_position_in_map(position, map_grid):

    x_index = position[0]
    y_index = position[1]

    if x_index < 0 or x_index >= len(map_grid):
        return False
    if y_index < 0 or y_index >= len(map_grid[0]):
        return False
    
    return True

def get_guard_direction(guard_character):

    if guard_character == '^':
        return Direction.Up
    elif guard_character == '<':
        return Direction.Left
    elif guard_character == '>':
        return Direction.Right
    elif guard_character == 'v':
        return Direction.Down

def get_next_guard_position(guard_poisition, map_grid):

    x_pos = guard_poisition[0]
    y_pos = guard_poisition[1]
    facing_direction = get_guard_direction(map_grid[x_pos][y_pos])

    if facing_direction == Direction.Up:
        return x_pos - 1, y_pos
    if facing_direction == Direction.Left:
        return x_pos, y_pos - 1
    if facing_direction == Direction.Right:
        return x_pos, y_pos + 1
    else: #Down
        return x_pos + 1, y_pos
    
def is_obstacle_in_position(position, map_grid):

    character = map_grid[position[0]][position[1]]
    if character == '#':
        return True
    return False

def update_map_grid(position, new_char, map_grid):
    new_grid = []
    for row_i in range(0, len(map_grid)):
        new_row = []
        for col_i in range(0, len(map_grid[row_i])):
            if row_i == position[0] and col_i == position[1]:
                new_row.append(new_char)
            else:
                new_row.append(map_grid[row_i][col_i])
        new_grid.append(new_row)
    return new_grid

def rotate_guard(guard_position, map_grid):

    x_pos = guard_position[0]
    y_pos = guard_position[1]
    direction = get_guard_direction(map_grid[x_pos][y_pos])

    if direction == Direction.Up:
        map_grid = update_map_grid(guard_position, '>', map_grid)
    elif direction == Direction.Right:
        map_grid = update_map_grid(guard_position, 'v', map_grid)
    elif direction == Direction.Down:
        map_grid = update_map_grid(guard_position, '<', map_grid)
    elif direction == Direction.Left:
        map_grid = update_map_grid(guard_position, '^', map_grid)

    return map_grid

def move_guard(current_pos, next_pos, map_grid):

    guard_char = map_grid[current_pos[0]][current_pos[1]]

    map_grid = update_map_grid(next_pos, guard_char, map_grid)
    map_grid = update_map_grid(current_pos, '@', map_grid)

    return map_grid
        

def print_map(map_grid):
    print("/////////===////////===////////")
    for row in map_grid:
        print(row)
    


def map_out_guard_movements(map_grid, guard_starting_position):

    guard_pos = guard_starting_position

    while is_position_in_map(guard_pos, map_grid):
        #print_map(map_grid)

        next_position = get_next_guard_position(guard_pos, map_grid)

        if not is_position_in_map(next_position, map_grid):
            map_grid[guard_pos[0]][guard_pos[1]] = '@'
            #print_map(map_grid)
            break

        if is_obstacle_in_position(next_position, map_grid):
            map_grid = rotate_guard(guard_pos, map_grid)
        else:
            map_grid = move_guard(guard_pos, next_position, map_grid)
            guard_pos = next_position
        
    return map_grid


def get_guard_positions_count(map_grid):
    count = 0
    for row in map_grid:
        for char in row:
            if char == '@':
                count += 1
    return count


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)
    map_grid = get_map_grid(lines)

    guard_pos = get_guard_position(map_grid)
    print("Guard position: ", guard_pos)

    map_grid = map_out_guard_movements(map_grid, guard_pos)
    positions_count = get_guard_positions_count(map_grid)
    print("Positions visited by guard: ", positions_count)

    

    
