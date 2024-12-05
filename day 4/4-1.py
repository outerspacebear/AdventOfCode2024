import re

def get_lines(input_file):

    lines = []

    for line in input_file:
        lines.append(line.split())

    return lines

def get_word_grid(lines):

    rows = []
    row_index = 0
    for line in lines:
        row = list(line)[0]
        #print(row[0])
        rows.append(row)

    #print(rows)
    return rows


def get_all_x_locations(letter_grid):

    x_locations = []

    for row_index in range(0, len(letter_grid)):
        row = letter_grid[row_index]
        #print(row)
        for col_index in range(0, len(row)):
            if row[col_index] == 'X':
                found_location = [row_index, col_index]
                x_locations.append(found_location)
                #print(found_location)

    return x_locations


def is_xmas_hor_str(letter_grid, x_location):

    row = letter_grid[x_location[0]]

    col = x_location[1]
    if len(row) < col + 4:
        return False
    
    if row[col + 1] == 'M' and row[col + 2] == 'A' and row[col + 3] == 'S':
        return True
    return False


def is_xmas_hor_rev(letter_grid, x_location):

    row = letter_grid[x_location[0]]

    col = x_location[1]
    if col < 3:
        return False
    
    if row[col - 1] == 'M' and row[col - 2] == 'A' and row[col - 3] == 'S':
        return True
    return False

def is_xmas_ver_str(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if len(letter_grid) < row + 4:
        return False
    
    if letter_grid[row + 1][col] == 'M' and letter_grid[row + 2][col] == 'A' and letter_grid[row + 3][col] == 'S':
        return True
    return False

def is_xmas_ver_rev(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if row < 3:
        return False
    
    if letter_grid[row - 1][col] == 'M' and letter_grid[row - 2][col] == 'A' and letter_grid[row - 3][col] == 'S':
        return True
    return False

def is_xmas_diag_bot_right(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if len(letter_grid) < row + 4 or len(letter_grid[row]) < col + 4:
        return False
    
    if letter_grid[row + 1][col + 1] == 'M' and letter_grid[row + 2][col + 2] == 'A' and letter_grid[row + 3][col + 3] == 'S':
        return True
    return False

def is_xmas_diag_top_left(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if row < 3 or col < 3:
        return False
    
    if letter_grid[row - 1][col - 1] == 'M' and letter_grid[row - 2][col - 2] == 'A' and letter_grid[row - 3][col - 3] == 'S':
        return True
    return False

def is_xmas_diag_top_right(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if row < 3 or len(letter_grid[row]) < col + 4:
        return False
    
    if letter_grid[row - 1][col + 1] == 'M' and letter_grid[row - 2][col + 2] == 'A' and letter_grid[row - 3][col + 3] == 'S':
        return True
    return False

def is_xmas_diag_bot_left(letter_grid, x_location):

    row = x_location[0]
    col = x_location[1]

    if len(letter_grid) < row + 4 or col < 3:
        return False
    
    if letter_grid[row + 1][col - 1] == 'M' and letter_grid[row + 2][col - 2] == 'A' and letter_grid[row + 3][col - 3] == 'S':
        return True
    return False


def get_xmas_count_at_location(letter_grid, x_location):

    count = 0

    if is_xmas_hor_str(letter_grid, x_location):
        count += 1
    if is_xmas_hor_rev(letter_grid, x_location):
        count += 1
    if is_xmas_ver_str(letter_grid, x_location):
        count += 1
    if is_xmas_ver_rev(letter_grid, x_location):
        count += 1
    if is_xmas_diag_bot_right(letter_grid, x_location):
        count += 1
    if is_xmas_diag_top_left(letter_grid, x_location):
        count += 1
    if is_xmas_diag_top_right(letter_grid, x_location):
        count += 1
    if is_xmas_diag_bot_left(letter_grid, x_location):
        count += 1

    if(count > 0):
        print("Count ", count, " at location ", x_location)

    return count


def get_xmas_count(letter_grid, x_locations):
    count = 0
    
    for x_location in x_locations:
        count_at_location = get_xmas_count_at_location(letter_grid, x_location)
        count += count_at_location

    return count
            

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)
    letter_grid = get_word_grid(lines)
    x_locations = get_all_x_locations(letter_grid)
    count = get_xmas_count(letter_grid, x_locations)

    print("XMAS Count: ", count)
    
