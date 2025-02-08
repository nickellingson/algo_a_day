class MergeSort:

    def merge(self, arr, s, m, e):
        # merge in place

        # copy the sorted left and right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # one of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    def merge_sort(self, arr, s, e):
        # recursive, split in half all of the way to singles
        # 1234
        # 12 34
        # 1 2 3 4

        # base case 
        if e - s + 1 <= 1:
            return arr
        
        # the middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.merge_sort(arr, s, m)

        # Sort the right half
        self.merge_sort(arr, m + 1, e)

        # Merge sorted halfs
        self.merge(arr, s, m, e)
        
        return arr




if __name__=="__main__":
    array= [1,2,4,7,9,10,5,4,6,1,7,8,3]
    m = MergeSort()
    print(m.merge_sort(array, 0, len(array) - 1))