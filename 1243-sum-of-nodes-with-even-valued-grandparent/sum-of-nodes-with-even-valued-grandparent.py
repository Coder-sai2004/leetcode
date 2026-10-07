# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        res = []
        def check(root):
            if root is None:
                return 

            if root.val % 2 == 0:
                
                if root.left:
                    a = root.left.left.val if root.left.left else 0
                    b = root.left.right.val if root.left.right else 0
                    res.extend([a,b])
                
                if root.right:
                    
                    c = root.right.left.val if root.right.left else 0
                    d = root.right.right.val if root.right.right else 0
                    res.extend([c,d])

            check(root.left)
            check(root.right)
        
        check(root)
        return sum(res)