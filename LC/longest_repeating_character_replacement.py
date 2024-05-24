class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        map = {}

        for i in range(len(s)):

            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
            
            while (i - left + 1) - max(map.values()) > k:
                map[s[left]] -= 1
                left += 1


            res = max(res, i - left + 1)

        return res