def merge_two_lists(l_one, l_two):
    merged_list = []
    i, j = 0, 0

    while i < len(l_one) and j < len(l_two):
        if l_one[i] < l_two[j]:
            merged_list.append(l_one[i])
            i += 1
        else:
            merged_list.append(l_two[j])
            j += 1

    while i < len(l_one):
        merged_list.append(l_one[i])
        i += 1

    while j < len(l_two):
        merged_list.append(l_two[j])
        j += 1

    return merged_list

def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            l_one = lists[i]
            l_two = lists[i + 1] if (i + 1) < len(lists) else []
            merged_lists.append(merge_two_lists(l_one, l_two))

        lists = merged_lists

    return lists[0]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)



lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
