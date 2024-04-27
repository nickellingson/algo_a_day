from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # list of 26 0's -> a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1

            # [1, 1, 0 ... 1]

            res[tuple(count)].append(s)
            
            # (1, 1, 0 ... 1) : ["bat"]

            # (1, 0, 0 ... 1) : ["eat"]
            # (1, 0, 0 ... 1) : ["eat","tea"]
        return res.values()

        # O(m * n)