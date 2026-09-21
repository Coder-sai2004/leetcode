# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        res = []
        def order(root,level,res):
            if root is None:
                return 
            if root.left is None and root.right is None:
                res.append(level)
            order(root.left,level + 1,res)
            order(root.right,level + 1,res)
        
        order(root,1,res)
        if res:
            return min(res)
        return 0