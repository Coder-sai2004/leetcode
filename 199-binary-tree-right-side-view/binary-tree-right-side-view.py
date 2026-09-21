# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []

        def invert(root):
            if root is None:
                return 
            
            root.left,root.right = root.right,root.left
            invert(root.left)
            invert(root.right)

        def right(root,level,res):
            if root is None:
                return 

            if len(res) == level:
                res.append(root.val)

            right(root.left,level + 1,res)
            right(root.right,level + 1,res)

    
        invert(root)
        right(root,0,res)
        
        return res