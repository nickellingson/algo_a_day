# Static array implementation and useful operations

# Insert on the end of an array
# length is values in array
# capacity is the max amount of values in an array
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

# Remove from end of an array
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
        length -= 1

def insertMiddle(arr, n, i, length, capacity):
    if length + 1 < capacity:
        for index in range(length - 1, i - 1, -1):
            arr[index + 1] = arr[index]

        arr[i] = n

def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[i - 1] = arr[index]

def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])