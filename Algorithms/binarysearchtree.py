class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    


def insert(node, value):
    # If tree is empty, return a new node
    if node is None:
        return Node(value)
    
    # Otherwise, recur down the tree
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    
    # Return the (unchanged) node pointer
    return node


def search(root, value):

    # If tree is empty return a new node or value is present at root
    if root is None or root.value == value:
        return root
    
    # value is smaller than root's value
    if value < root.value:
        search(root.left, value)
    
    # value is larger than root's value
    return search(root.right, value)
    


# Driver Code
if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
 
    # value to be found
    value = 6
 
    # Searching in a BST
    if search(root, value) is None:
        print(value, "not found")
    else:
        print(value, "found")
 
    value = 60
 
    # Searching in a BST
    if search(root, value) is None:
        print(value, "not found")
    else:
        print(value, "found")


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print(binary_search_path(root, 4))