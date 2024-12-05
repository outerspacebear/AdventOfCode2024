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


def get_updates_following_rules(updates, rules):

    result_updates = []

    for update in updates:
        if is_update_following_rules(update, rules):
            result_updates.append(update)

    return result_updates


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
    updates_following_rules = get_updates_following_rules(updates, rules)
    print("Number of updates following rules: ", len(updates_following_rules))
    print(updates_following_rules)
    
    sum = get_sum_of_middle_numbers(updates_following_rules)
    print("Sum of updates following rules: ", sum)

    
