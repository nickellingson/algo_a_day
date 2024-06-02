# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):

            if not root:
                return [True, 0]

            # call helper on children
            left = helper(root.left)
            right = helper(root.right)

            # check if existing branches are not balanced
            # check current branch to make sure balanced
            balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return boolean balance variable and height
            return [balance, max(left[1], right[1]) + 1]

        return helper(root)[0]