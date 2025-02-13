# shortest path from top left to bottom right
# layer by layer
# O(n * m)
from collections import deque

def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    # top left
    queue.append((0, 0)) # use tuple for coordinates
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            # reached bottom right
            if r == ROWS - 1 and c == COLS - 1:
                return length
            
            neighbors = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or # out of bounds (min)
                    r + dr == ROWS or c + dc == COLS or # out of bounds (max)
                    (r + dr, c + dc) in visit or # already visited
                    grid[r + dr][c + dc] == 1): # blocked (value 1)
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

print(bfs(grid)) # 6


