# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        res = {}

        def check(root,level):
            if root is None:
                return 

            if len(res) <= level:
                res[level] = 0

            res[level] += root.val

            check(root.left,level + 1)
            check(root.right,level + 1)

        check(root,0)

        ans = max(res,key = res.get)
        return ans + 1