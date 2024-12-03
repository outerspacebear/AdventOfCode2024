import re

def get_lines(input_file):

    lines = []

    for line in input_file:
        lines.append(line.split())

    return lines


def get_str_start_mul_numbers(string):
    numbers = re.search('(([0-9]+),([0-9]+))', string)
    print(numbers)

    if numbers != None:
        #print(numbers.span()[0])
        if numbers.span()[0] != 1:
            return None
        elif string[numbers.span()[0] - 1] != '(' or string[numbers.span()[1]] != ')':
            return None
        
        print(numbers.group())
        match_str = str(numbers.group())
        mul_numbers = match_str.split(',')
        return mul_numbers
    
    return None
        

def get_mul_instructions_in_line(input_line):
    result = 0

    line_splits = input_line.split("mul")
    for split_str in line_splits:
        print("=======\n", split_str)
        numbers_to_multiply = get_str_start_mul_numbers(split_str)
        if numbers_to_multiply != None:
            mul = int(numbers_to_multiply[0]) * int(numbers_to_multiply[1])
            result += mul

    return result
            

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)

    final_result = 0

    for input_line in lines:
        mul_result = get_mul_instructions_in_line(str(input_line))
        final_result += mul_result
    print("Final result: ", final_result)
    
