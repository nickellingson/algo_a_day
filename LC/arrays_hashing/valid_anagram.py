
from collections import Counter

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] > 0:
                return False
        return True
    
# More solutions


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)