class Solution:

    def remove_elements(self, nums, val):
        count = 0
        for i in range(len(nums)):
            
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            
        return count

sol = Solution()
print(sol.remove_elements([1,2,3,4,5], 3))