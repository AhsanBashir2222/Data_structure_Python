def insertion(list):
    index_len = range(1, len(list))
    for i in index_len:
        value_to_sort = list[i]

        while list[i-1] > value_to_sort and i > 0:
            list[i], list[i-1] = list[i-1], list[i]
            i = i-1

    return list


print(insertion([7, 5, 4, 3, 2, 2]))
