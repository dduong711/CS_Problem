# solution.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
            wr = []
            pre = [TreeNode(-float("inf")), ]
            self.check(root, pre, wr)
            if len(wr) == 1:
                wr[0][0].val, wr[0][1].val = wr[0][1].val, wr[0][0].val
            else:
                wr[0][0].val, wr[1][1].val = wr[1][1].val, wr[0][0].val

    def check(self, root, pre, wr):
        if root != None:
            self.check(root.left, pre, wr)
            if pre[-1].val > root.val:
                wr.append([pre[-1], root])
            pre[-1] = root
            self.check(root.right, pre, wr)