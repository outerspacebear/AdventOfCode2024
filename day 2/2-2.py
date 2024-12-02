
def get_lines(input_file):

    lines = []

    for line in input_file:
        lines.append(line.split())

    return lines

def is_report_safe(report_line):

    has_increased = False
    has_decreased = False
    previous_level = -1

    for level_str in report_line:
        level = int(level_str)
        
        if(previous_level == -1):
            previous_level = level
            continue
        
        if level > previous_level:
            has_increased = True
        elif level < previous_level:
            has_decreased = True
        else:
            return False
        
        if (has_increased and has_decreased):
            return False
        
        difference = abs(level - previous_level)
        if(difference > 3 or difference < 1):
            return False
        
        previous_level = level

    return True


def is_report_safe_with_problem_dampener(report_line):

    if is_report_safe(report_line):
        return True

    print(report_line)

    for i in range(0, len(report_line)):
        report_without_current_level = report_line.copy()
        report_without_current_level.pop(i)

        print("\t==> ", report_without_current_level)

        if is_report_safe(report_without_current_level):
            return True
        
    #print(report_line, "  ====\n")
    return False


def get_number_of_safe_reports(reports_lines):

    safe_reports_count = 0

    for report_line in reports_lines:
        #print(report_line)
        is_safe = is_report_safe_with_problem_dampener(report_line)
        print(is_safe)
        if is_safe:
            safe_reports_count += 1

    return safe_reports_count


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    lines = get_lines(input_file)

    number_of_safe_reports = get_number_of_safe_reports(lines)
    print("Number of safe reports: ", number_of_safe_reports)
    
