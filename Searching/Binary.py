def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid+1
        if arr[mid] > target:
            right = mid-1

    return -1


mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 5
result = binary_search(mylist, x)
if result != -1:
    print("Found at index : ", result)
else:
    print("Not Found")
