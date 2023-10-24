# Route Planning
# Shortest path
# Similar to brute force, but uses values to find order that makes sense
import heapq

def shortestPath(n, edges, src):
    adj = {}
    for i in range(n):
        adj[i] = []

    for s, d, weight, in edges:
        adj[s].append([d, weight])
    
    shortest = {} # Map vertex -> dist of shortest path
    minHeap = [[0, src]]
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2, in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, [w1 + w2, n2])

    for i in range(n):
        if i not in shortest:
            shortest[i] = -1


    return shortest

edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
print(shortestPath(5, edges, 0))