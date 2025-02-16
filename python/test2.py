# Core python
# 1
def double_elements(lst):
    new_lst = [x * 2 for x in lst]
    return new_lst

print(double_elements([1, 2, 3, 4, 5]))

# 2
def lookup_key(d, key):
    if key in d:
        return d[key]
    else:
        return "Key not found."
print(lookup_key({"hello":1, "hi": 2}, "hello"))

# Algorithms
# 1
def merge_sort(lst, s, e):
# base case e - s + 1 equal to or less than 0, return list
# call sort on split lists
# merge on both lists
# return list
# copy lists and then while loop, check value and merge
# two more while loops to clean up the non empty one

    if e - s + 1 <= 1:
        return lst
    
    # middle index
    m = (s + e) // 2

    # sort the left half
    merge_sort(lst, s, m)

    # sort the right half
    merge_sort(lst, m + 1, e)

    # merge sorted halfs
    merge(lst, s, m, e)

    return lst

def merge(lst, s, m, e):
    # Copy the sorted left and right halfs to temp arrays
    L = lst[s: m + 1]
    R = lst[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    
    # one of the halfs will have elements remaining
    while i < len(L):
        lst[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        lst[k] = R[j]
        j += 1
        k += 1
print(merge_sort([5, 4, 3, 2, 1], 0, 4))
    

# 2 
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (right + left) // 2
        if arr[middle] > target:
            right = middle - 1
        elif arr[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))