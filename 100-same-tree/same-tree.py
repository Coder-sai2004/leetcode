# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        r1 = []
        r2 = []
        def order(root,res):
            if root is None:
                res.append(None)
                return 

            res.append(root.val)

            order(root.left,res)
            order(root.right,res)

        order(p,r1)
        order(q,r2)

        return r1 == r2