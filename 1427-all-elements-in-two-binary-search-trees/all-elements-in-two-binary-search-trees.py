# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        res = []
        def check(root):
            if root is None:
                return 

            res.append(root.val)

            check(root.left)
            check(root.right)

        check(root1)
        check(root2)

        return sorted(res)