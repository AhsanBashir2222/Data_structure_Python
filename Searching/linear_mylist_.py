# list
mylist = [1, 2, 3, 4, 5, 6, 7]
if 4 in mylist:
    print("Found")
else:
    print("Not Found")

# linear


def linear_search(arr, Target):
    for i in range(len(arr)):
        if arr[i] == Target:
            return i
    return -1


myarr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5
myresult = linear_search(myarr, x)
if myresult != -1:
    print("Found at index : ", myresult)
else:
    print("Not Found")
