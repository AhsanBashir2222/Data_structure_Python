def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    l_half = arr[:mid]
    R_half = arr[mid:]
    l_half = merge_sort(l_half)
    R_half = merge_sort(R_half)
    return merge(l_half, R_half)


def merge(left, right):
    new = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1

        else:
            new.append(right[j])
            j += 1

    new.extend(left[i:])
    new.extend(right[j:])
    return new


mylist = [10, 7, 2, 6, 10, 15, 12, 13, 55, 12]
mysorted = merge_sort(mylist)
print("Sorted Array : ", mysorted)
