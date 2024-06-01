 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        # height of left + height of right
        def dfs(root):
            if not root:
                return 0

            # recursion
            left = dfs(root.left)
            right = dfs(root.right)
            
            # diameter
            nonlocal diameter
            diameter = max(diameter, left + right)

            # height
            return 1 + max(left, right)
        
        # call function
        dfs(root)

        return diameter