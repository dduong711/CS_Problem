# solution.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.solution(root)[-1]
        
    def solution(self, node):
        if not node:
            return (float("inf"), -float("inf"), 0)
        else:
            mil, mal, mdl = self.solution(node.left)
            mir, mar, mdr = self.solution(node.right)
            return (
                min(mil, mir, node.val),
                max(mal, mar, node.val),
                max(
                    mdl,
                    mdr,
                    abs(node.val - min(mil, mir, node.val)),
                    abs(node.val - max(mal, mar, node.val)),
                )
            )
