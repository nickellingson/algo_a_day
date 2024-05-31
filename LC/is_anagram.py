class Solution:

# edge cases
# a ab
# ab a

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
            
        t_map = {}
        for j in t:
            if j in t_map:
                t_map[j] += 1
            else:
                t_map[j] = 1
        
        for key, val in s_map.items():
            if key in t_map:
                if t_map.get(key) != val:
                    return False
            else:
                return False
        return True