def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                swap = list[j]
                list[j] = list[j+1]
                list[j+1] = swap
    return list

print(sort([1,2,65,4,78,3,4,4,10]))