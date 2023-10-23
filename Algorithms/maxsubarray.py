class Solution:

    def maxSubArray(self, nums):
        if (not nums):
            return 0
        maxSubArray = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSubArray = max(maxSubArray, curSum)
        return maxSubArray
    
test = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(test.maxSubArray(nums))