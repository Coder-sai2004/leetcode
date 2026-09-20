# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = []

        def pre(root):
            if root is None:
                return 

            pre(root.left)
            res.append(root.val)
            pre(root.right)
            
        pre(root)
        return res[k-1]