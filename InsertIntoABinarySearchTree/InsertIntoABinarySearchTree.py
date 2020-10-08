# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        node = root
        while node != None:
            s = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if s.val < val:
            s.right = TreeNode(val)
        else:
            s.left = TreeNode(val)
        return root