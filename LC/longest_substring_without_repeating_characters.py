class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        left = 0
        res = 0

        for i in range(len(s)):

            while s[i] in map:
                map.remove(s[left])
                left += 1

            map.add(s[i])
            res = max(res, i - left + 1)

        return res