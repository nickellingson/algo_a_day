# Recursive Python program for level
# DFS
 
# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# DFS
def print_dfs_tree(node):
    if node:
        print_dfs_tree(node.left)
        print(node.data)
        print_dfs_tree(node.right)

 
 
# Driver program to test above function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_dfs_tree(root)