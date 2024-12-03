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
        

def get_mul_instructions_in_line(input_line, is_enabled_param):
    result = 0

    is_enabled = is_enabled_param

    line_splits = input_line.split("mul")
    for split_str in line_splits:
        print("=======\n", split_str)

        if not is_enabled:
            print("Disabled!")
        else:
            numbers_to_multiply = get_str_start_mul_numbers(split_str)
            if numbers_to_multiply != None:
                mul = int(numbers_to_multiply[0]) * int(numbers_to_multiply[1])
                result += mul
        
        do_occurences = [m.start() for m in re.finditer('do\(\)', split_str)]
        dont_occurences = [m.start() for m in re.finditer('don\'t\(\)', split_str)]

        print("Do: ", do_occurences)
        print("Don't: ", dont_occurences)

        num_do = len(do_occurences)
        num_dont = len(dont_occurences)

        if(num_do == 0 and num_dont == 0):
            continue
        elif(num_do > 0 and num_dont == 0):
            is_enabled = True
            print("\t\t\t\t\t\t\t==> Enabling!")
        elif(num_dont > 0 and num_do == 0):
            is_enabled = False
            print("\t\t\t\t\t\t\t==> Disabling!")
        else:
            last_do = do_occurences[num_do - 1]
            last_dont = dont_occurences[num_dont - 1]
            if last_do > last_dont:
                is_enabled = True
                print("\t\t\t\t\t\t\t==> Enabling!")
            else:
                is_enabled = False
                print("\t\t\t\t\t\t\t==> Disabling!")


    return result, is_enabled
            

if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)

    final_result = 0

    is_enabled = True

    for input_line in lines:
        mul_result, is_enabled = get_mul_instructions_in_line(str(input_line), is_enabled)
        final_result += mul_result
    print("Final result: ", final_result)
    
