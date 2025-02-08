
class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) >= 2:
            stones.sort()
            heaviest = stones.pop()
            heaviest_2 = stones.pop()
            if heaviest != heaviest_2:
                stones.append(heaviest - heaviest_2)
        if stones:
            return stones[0]
        else:
            return 0