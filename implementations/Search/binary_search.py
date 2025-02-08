class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def search(self, arr, key):
        # take start index and last index
        # loop through, find the middle index
        # middle index is greater than key, move max down, vice versa

        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (r + l) // 2

            # move upper pointer past middle
            if arr[m] > key:
                r = m - 1
            # move lower pointer past middle
            elif arr[m] < key:
                l = m + 1
            else:
                return m
        # not found
        return -1
    
if __name__=="__main__":
    bs = BinarySearch([1,2,3,4,5,6,7,8,9,10,11])
    print(bs.search(bs.arr, 2))