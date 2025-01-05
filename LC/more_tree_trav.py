class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def dfs_w_height_traversal(self, root, height):

        if not root:
            return None
        
        # if height == 0:
        #     # print(root.val)
        
        # if height >= 1:
        #     # print(root.val, end=" ")

        print(height, root.val)
        self.dfs_w_height_traversal(root.left, height + 1)
        self.dfs_w_height_traversal(root.right, height + 1)

root = Node(1)
left = Node(2)
right = Node(3)
left_left = Node(4)
left_right = Node(5)
root.left = left
root.right = right
root.left.left = left_left
root.left.right = left_right

#    1 
#  2   3
# 4 5

# sol = Solution()
# sol.dfs_w_height_traversal(root, 0)



from collections import deque

class Node2:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



class IterativeSolution:

    def print_q(self, q):
        for c in q:
            print(c.val, end=" ")
        print("")


    def level_order_trav_iter(self, root, height):
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):

                curr_node = q.popleft()
                # print("pop", curr_node.val)
                print(curr_node.val, end=" ")
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            print("")
            level += 1  
        return level



#        1 
#     2       3
#   4   5    6   7
#  8 9 10 11



root = Node2(1)
left = Node2(2)
right = Node2(3)
left_left = Node2(4)
left_right = Node2(5)
right_left = Node(6)
right_right = Node2(7)
left_left_left = Node2(8)
left_left_right = Node2(9)
left_right_left = Node(10)
root.left = left
root.right = right
root.left.left = left_left
root.left.right = left_right
root.right.left = right_left
root.right.right = right_right
root.left.left.left = left_left_left
root.left.left.right = left_left_right
root.left.right.left = left_right_left


bfs = IterativeSolution()

bfs.level_order_trav_iter(root, 0)








# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
 
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# Function to print level order traversal of a tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)

# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)