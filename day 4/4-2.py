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


def get_all_a_locations(letter_grid):

    x_locations = []

    for row_index in range(0, len(letter_grid)):
        row = letter_grid[row_index]
        #print(row)
        for col_index in range(0, len(row)):
            if row[col_index] == 'A':
                found_location = [row_index, col_index]
                x_locations.append(found_location)
                print(found_location)

    return x_locations


def is_x_mas_at_loc(letter_grid, a_location):

    row = a_location[0]
    col = a_location[1]

    if row < 1 or col < 1 or row == len(letter_grid) - 1 or col == len(letter_grid[row]) - 1:
        return False
    
    top_left_bot_right_mas = False
    bot_left_top_right_mas = False

    if (letter_grid[row-1][col-1] == 'M' and letter_grid[row + 1][col + 1] == 'S') or (letter_grid[row-1][col-1] == 'S' and letter_grid[row + 1][col + 1] == 'M'):
        top_left_bot_right_mas = True
    
    if (letter_grid[row+1][col-1] == 'M' and letter_grid[row - 1][col + 1] == 'S') or (letter_grid[row+1][col-1] == 'S' and letter_grid[row - 1][col + 1] == 'M'):
        bot_left_top_right_mas = True

    return top_left_bot_right_mas and bot_left_top_right_mas


def get_xmas_count_at_location(letter_grid, a_location):

    count = 0

    if is_x_mas_at_loc(letter_grid, a_location):
        count += 1

    if(count > 0):
        print("Count ", count, " at location ", a_location)

    return count


def get_xmas_count(letter_grid, a_locations):
    count = 0
    
    for a_location in a_locations:
        count_at_location = get_xmas_count_at_location(letter_grid, a_location)
        count += count_at_location

    return count
            

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)
    letter_grid = get_word_grid(lines)
    a_locations = get_all_a_locations(letter_grid)
    count = get_xmas_count(letter_grid, a_locations)

    print("XMAS Count: ", count)
    
