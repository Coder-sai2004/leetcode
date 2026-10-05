# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def check(node,t,s):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                s += node.val
                if s == t:
                    return True
                

            l = check(node.left,t,s + node.val)
            r = check(node.right,t,s + node.val)

            if l or r:
                return True
            return False

        if root is None:
            return False
        return check(root,targetSum,0)