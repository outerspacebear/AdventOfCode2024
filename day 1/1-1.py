
def get_lists(input_file):

    list_1 = []
    list_2 = []

    for line in input_file:
        location_id_1, location_id_2 = line.split()
        list_1.append(location_id_1)
        list_2.append(location_id_2)

    return list_1, list_2
    
def get_list_of_differences_in_values(list_1, list_2):

    list_of_differences = []

    for i in range(min(len(list_1), len(list_2))):
        element_1, element_2 = list_1[i], list_2[i]
        difference = int(element_1) - int(element_2)
        #print(element_1, element_2, difference)
        list_of_differences.append(abs(difference))

    return list_of_differences


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    list_1, list_2 = get_lists(input_file)

    #print("List 1: ", list_1, "\nList 2: ", list_2)

    list_1.sort()
    list_2.sort()

    #print("Sorted list 1: ", list_1, "\nSorted list 2: ", list_2)

    #print("List lengths: ", len(list_1), len(list_2))

    list_of_differences = get_list_of_differences_in_values(list_1, list_2)
    print("Sum of differences: ", sum(list_of_differences))
