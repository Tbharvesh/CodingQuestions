# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,root,target):
        if not root:
            return 
        
        root.left = self.rec(root.left , target)
        root.right = self.rec(root.right , target) 
        if not root.left and not root.right and root.val == target :
            return None

        return root

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.rec(root,target)