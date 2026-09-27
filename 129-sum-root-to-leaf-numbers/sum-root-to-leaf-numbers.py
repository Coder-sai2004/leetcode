# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def order(root,x,ans):
            if root is None:
                return 0

            if root.left is None and root.right is None:
                x += str(root.val)
                return int(x)
            else:
                x += str(root.val)

            l = order(root.left,x,ans)
            r = order(root.right,x,ans)

            return ans + l + r

        return order(root,'',0)
        