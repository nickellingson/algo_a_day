class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:

            middle = (right_index + left_index) // 2

            if nums[middle] > target:
                right_index = middle - 1

            elif nums[middle] < target:
                left_index = middle + 1

            else:
                return middle

        return -1