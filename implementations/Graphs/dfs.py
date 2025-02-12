
class GraphNode:

    def __init__(self, val):
        self.val = val
        self.neighbors = []

# count the unique paths from top left of grid to bottom right of grid
# Count paths (backtracking) O(4 ^ n * m), Mem O(n*m) or size of visited hash set
grid = [[0,0,0,0],[1,1,0,0],[0,0,0,1],[0,1,0,0]]

def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or # out of bounds, minumum
        r == ROWS or c == COLS or # out of bounds, maximum
        (r, c) in visit or grid[r][c] == 1): # already visited or blocked (equal to 1)
        return 0
    
    # reach destination
    if r == ROWS - 1 and c == COLS - 1:
        return 1
    
    # add tuple to set as visited
    visit.add((r,c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count

# every function call uses same set, passing in reference to the same object
print(dfs(grid, 0, 0, set()))