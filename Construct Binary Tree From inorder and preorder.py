# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, hp):
        if preStart > preEnd or inStart > inEnd:
            return None
        root = TreeNode(preorder[preStart])
        # Position of root in inorder
        inRoot = hp[root.val]
        # No. of elem on the left of root
        numLeft = inRoot - inStart
        # Traverse all th elem from left to root
        root.left = self.buildTree(
            preorder, preStart + 1, preStart + numLeft, inorder, inStart, inRoot - 1, hp
        )
        root.right = self.buildTree(
            preorder, preStart + numLeft + 1, preEnd, inorder, inRoot + 1, inEnd, hp
        )
        return root

    def bstFromPreorder(self, li: List[int]) -> Optional[TreeNode]:
        if not li:
            return
        inorder = sorted(li)
        # Creating hashmap for storing the index/pos of inorder traversal
        hp = dict()
        for i in range(len(li)):
            hp[inorder[i]] = i

        root: TreeNode = self.buildTree(li, 0, len(li) - 1, inorder, 0, len(inorder) - 1, hp)
        return root
