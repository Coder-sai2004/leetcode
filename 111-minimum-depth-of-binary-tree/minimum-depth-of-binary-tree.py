# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        res = float('inf')


        def order(root,level):
            if root is None:
                return float('inf')

            if root.left is None and root.right is None:
                return level

            left = order(root.left,level + 1)
            right = order(root.right,level + 1)

            return min(left,right)
        
        if root is None:
            return 0
        return order(root,1)