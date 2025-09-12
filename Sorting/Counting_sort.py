def countinfsort(arr):
    max_value = max(arr)
    count = [0]*(max_value+1)
    while len(arr):
        num = arr.pop(0)
        count[num] += 1

        for i in range(len(count)):
            while count[i] > 0:
                arr.append(i)
                count[i] -= 1
        return arr


mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortlist = countinfsort(mylist)
print(mysortlist)
