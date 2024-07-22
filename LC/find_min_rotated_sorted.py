class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        minum = nums[low]
        while low <= high:
            if nums[low] < nums[high]:
                if minum > nums[low]:
                    minum = nums[low]
                break
            middle = (high + low) // 2
            minum = min(minum, nums[middle])
            if nums[middle] >= nums[low]:
                low = middle + 1
            else:
                high = middle - 1
            
        return minum