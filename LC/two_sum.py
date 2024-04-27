class Solution:
    def twoSum(self, nums, target: int):
        dict = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result not in dict:
                dict[nums[i]] = i
            else:
                return [dict[result], i]
        return -1
