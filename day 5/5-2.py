import re

def get_lines(input_file):

    lines = []

    for line in input_file:
        lines.append(line.strip())

    return lines

def get_rules_and_updates(lines):

    rules = []

    break_line_index = 0
    for i in range (0, len(lines)):
        line = lines[i]
        if line == "":
            break_line_index = i
            break

        print(line)
        rule_pair = str(line).split('|')
        print(rule_pair)
        rules.append(rule_pair)
    
    updates = []

    for i in range(break_line_index + 1, len(lines)):
        line = lines[i]
        update_order = str(line).split(",")
        updates.append(update_order)

    return rules, updates


def get_rules_involving_numbers_in_update(update, rules):
    result_rules = []

    for rule in rules:
        if (rule[0] in update) and (rule[1] in update):
            result_rules.append(rule)

    return result_rules


def is_update_following_rules(update, rules):

    rules_for_update = get_rules_involving_numbers_in_update(update, rules)

    for rule in rules_for_update:
        first_num = rule[0]
        second_num = rule[1]
        first_index = update.index(first_num)
        second_index = update.index(second_num)

        if first_index > second_index:
            return False
        
    return True


def get_updates_following_an_not_rules(updates, rules):

    result_updates = []
    updates_not_following_rules = []

    for update in updates:
        if is_update_following_rules(update, rules):
            result_updates.append(update)
        else:
            updates_not_following_rules.append(update)

    return result_updates, updates_not_following_rules


def correct_update_not_following_rules(update, rules):

    rules_for_update = get_rules_involving_numbers_in_update(update, rules)

    corrected_update = update.copy()
    while (not is_update_following_rules(corrected_update, rules_for_update)):
        for rule in rules_for_update:
            first_num = rule[0]
            second_num = rule[1]
            first_index = corrected_update.index(first_num)
            second_index = corrected_update.index(second_num)

            if(first_index > second_index):
                corrected_update[first_index] = second_num
                corrected_update[second_index] = first_num
                break
    
    print (update, " corrected to ", corrected_update)
    return corrected_update


def get_corrected_updates(updates, rules):
    corrected_updates = []
    for update in updates:
        corrected_updates.append(correct_update_not_following_rules(update, rules))
    return corrected_updates


def get_sum_of_middle_numbers(updates):

    sum = 0
    for update in updates:
        median_index = (len(update) - 1)/2
        print(median_index)
        median = update[int(median_index)]
        sum += int(median)

    return sum


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)
    rules, updates = get_rules_and_updates(lines)
    updates_following_rules, updates_not_following_rules = get_updates_following_an_not_rules(updates, rules)
    print("Number of updates following rules: ", len(updates_following_rules))
    print(updates_following_rules)
    
    sum = get_sum_of_middle_numbers(updates_following_rules)
    print("Sum of updates following rules: ", sum)

    corrected_updates = get_corrected_updates(updates_not_following_rules, rules)
    sum_corrected_updates = get_sum_of_middle_numbers(corrected_updates)
    print("Sum of corrected updates: ", sum_corrected_updates)


    
