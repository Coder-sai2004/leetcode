# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = []
        c = 1
        def pre(node, c):
            if node is None:
                return 

            if node.left is None and node.right is None:
                res.append(c)
                c = 0
            
            
            
            c += 1
            pre(node.left , c)
            pre(node.right , c)

        
        pre(root, c)

        return max(res)