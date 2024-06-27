# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree(self,postorder , ps, pe, inorder,ist ,ie ,hp) :
        if ps > pe or ist > ie:
            return None
        root = TreeNode(postorder[pe])
        indexOfRoot = hp[root.val]
        noElem = indexOfRoot - ist
        root.left = self.tree(postorder, ps ,ps + noElem - 1, inorder , ist ,indexOfRoot - 1,hp)
        root.right = self.tree(postorder, ps + noElem  , pe-1 , inorder , indexOfRoot + 1 ,ie,hp)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hp = dict()
        for i in range(len(inorder)):
            hp[inorder[i]] = i
        root : TreeNode = self.tree(postorder, 0, len(postorder)-1, inorder, 0 , len(inorder)-1 , hp)
        return root