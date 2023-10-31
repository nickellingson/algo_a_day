# RECURSIVE
# Returns index of x in arr if present, else -1
def recursive_binary_search(arr, low, high, x):
    
    # Check base case
    if high >= low:
        
        # Floor
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return recursive_binary_search(arr, low, mid - 1, x)
        
        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search(arr, mid + 1, high, x)
    
    # Element is not present in the array    
    else:
        return -1
    

# ITERATIVE
def iterative_binary_search(arr, x):
    low = 0
    high = arr.length-1
    middle = 0

    while low <= high:
        middle = (high+low)//2
        if arr[middle] == x:
            return middle
        elif arr[middle] > x:
            high = middle - 1
        else:
            low = middle + 1

    return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = recursive_binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")