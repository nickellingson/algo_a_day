class Solution:



    def remove_duplicates(self, nums):

        count = 0
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = True
                nums[count] = nums[i]
                count += 1
        
        return count




sol = Solution()

print(sol.remove_duplicates([1,1,1,2,2,2,3,3,3,4]))