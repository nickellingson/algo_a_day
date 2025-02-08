import heapq
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
        
    # max heap (need to make negative because there is only minheap)
    def otherSolutionHeap(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])

