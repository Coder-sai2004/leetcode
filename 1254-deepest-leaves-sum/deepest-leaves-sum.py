# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def deep(root):
            if root is None:
                return 0
            
            left_depth = deep(root.left)
            right_depth = deep(root.right)

            return 1 + max(left_depth,right_depth)

        def order(root,level,m,ans):
            if root is None:
                return ans
            
            if level == m:
                ans += root.val

            ans = order(root.left,level + 1,m,ans)
            ans = order(root.right,level + 1,m,ans)

            return ans
        
        m = deep(root)
        return order(root,1,m,ans)