class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix) - 1

        while low <= high:

            middle = (high + low) // 2

            if target > matrix[middle][-1]:
                low = middle + 1
            elif target < matrix[middle][0]:
                high = middle - 1
            else:
                break
        l = 0
        h = len(matrix[middle]) - 1
        arr = matrix[middle]

        while l <= h:
            
            m = (l + h) // 2

            if target > arr[m]:
                l = m + 1

            elif target < arr[m]:
                h = m  - 1
            
            else:
                return True
        return False