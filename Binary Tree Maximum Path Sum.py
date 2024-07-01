# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Inorder traversal of tree
class Solution:
    
    m = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            leftSum = max(rec(root.left) , 0)
            rightSum = max(rec(root.right) , 0)
            curSum = root.val + leftSum + rightSum
            self.m = max(self.m , curSum)
            return root.val + max(leftSum , rightSum)
        rec(root)
        return self.m
        