
def get_lists(input_file):

    list_1 = []
    list_2 = []

    for line in input_file:
        location_id_1, location_id_2 = line.split()
        list_1.append(location_id_1)
        list_2.append(location_id_2)

    return list_1, list_2


def get_similarity_scores_list(list_1, list_2):
    
    list_of_similarity_scores = []

    for i in range(min(len(list_1), len(list_2))):
        element_1 = list_1[i]
        element_1_count_in_list_2 = list_2.count(element_1)
        list_of_similarity_scores.append(int(element_1) * int(element_1_count_in_list_2))

    return list_of_similarity_scores


if __name__ == "__main__":

    input_file = open('input.txt', 'r')
    list_1, list_2 = get_lists(input_file)

    #print("List 1: ", list_1, "\nList 2: ", list_2)

    list_1.sort()
    list_2.sort()

    #print("Sorted list 1: ", list_1, "\nSorted list 2: ", list_2)

    #print("List lengths: ", len(list_1), len(list_2))

    list_of_similarity_scores = get_similarity_scores_list(list_1, list_2)
    print("Total similarity score: ", sum(list_of_similarity_scores))
