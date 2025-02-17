def merge_sort(array, s, e):

    # basecase, single element or none
    if e - s + 1 <= 1:
        return array
    
    # get middle
    m = (s + e) // 2

    # call on left and right sub lists recursively
    merge_sort(array, s, m)
    merge_sort(array, m + 1, e)

    merge(array, s, m , e)

    return array

def merge(array, s, m, e):

    # make copies of left and right subarrays
    L = array[s:m + 1] # need + 1 becuase inclusive, exclusive
    R = array[m+1:e+1]

    left = 0
    right = m + 1
    k = s

    # merge the two lists in order
    while left < len(L) and right < len(R):
        if L[left] > R[right]:
            array[k] = R[right]
            right += 1
        else:
            array[k] = L[left]
            left += 1
        k += 1
    
    # leftovers
    while left < len(L):
        array[k] = L[left]
        left += 1
        k += 1
    
    while right < len(R):
        array[k] = R[right]
        right += 1
        k += 1

# start and end indexes of array
print(merge_sort([9,8,7,6,5,4,3,2,1], 0, 8))