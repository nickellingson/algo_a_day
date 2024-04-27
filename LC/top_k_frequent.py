


class Solution:
    def topKFrequent(self, nums, k):
    
    # loop through elements and add to dict with corresponding appearances
    # loop through values of dict place values on array index = appearance and value = value
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        array = [[] for i in range(len(nums) + 1)]
        print(array)
        for key, value in dict.items():
            array[value].append(key)

        
        result = []
        for i in reversed(array):
            for j in i:
                print(j)
                result.append(j)
                if len(result) == k:
                    return result

# k = 2
# dict{1:3, 2:2, 3:1}
# array = [0,3,2,1,0,0]
# result = [1,2]
sol = Solution()
nums = [1,1,1,1,1,1,2,3,4,7,9,10,10]
print(sol.topKFrequent(nums, 4))