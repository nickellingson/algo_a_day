from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree:

    def __init__(self):
        self.root = TreeNode(10)
    
    def dfs(self, root):
        # recursive
        if not root:
            return None
        
        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)


    def bfs(self, root):
        # iterative
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                print(node.val, end="")
            print("")

if __name__=="__main__":
    t = Tree()
    t.root.left = TreeNode(20)
    t.root.right = TreeNode(30)
    t.root.left.left = TreeNode(40)
    t.root.left.right = TreeNode(50)
    t.root.left.left.left = TreeNode(60)

    t.dfs(t.root)
    t.bfs(t.root)