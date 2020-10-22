# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.minimum(root, 1)
    
    def minimum(self, node, depth):
        if node == None:
            return float("inf")
        if not node.left and not node.right:
            return depth
        else:
            return min(
                self.minimum(node.left, depth + 1), 
                self.minimum(node.right, depth + 1)
            )