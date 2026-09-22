# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = []
        ans = []
        def deep(root,level):
            if root is None:
                return 
            
            if root.left is None and root.right is None:
                res.append(level)

            deep(root.left,level + 1)
            deep(root.right,level + 1)

        def order(root,level,m):
            if root is None:
                return 
            
            if level == m:
                ans.append(root.val)

            order(root.left,level + 1,m)
            order(root.right,level + 1,m)
        
        deep(root,1)
        m = max(res)

        order(root,1,m)

        return sum(ans)