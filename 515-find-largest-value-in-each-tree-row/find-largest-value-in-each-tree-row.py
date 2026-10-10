# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        res = []

        def traverse(root,level):
            if root is None:
                return 
            
            if len(res) <= level:
                res.append(-2**31)

            res[level] = max(res[level],root.val)

            traverse(root.left,level + 1)
            traverse(root.right,level + 1)

        traverse(root,0)
        
        return res