# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        temp = []

        def check(node,t):
            if node is None:
                return
            
            temp.append(node.val)
            if node.left is None and node.right is None:
                if sum(temp) == t:
                    res.append(temp.copy())

            check(node.left,t)
            check(node.right,t)
            temp.pop()
            
        check(root,targetSum)
        return res