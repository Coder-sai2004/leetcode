# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def check(node,s,res):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                s += str(node.val)
                return int(s,2)


            l = check(node.left,s + str(node.val),res)
            r = check(node.right,s + str(node.val),res)

            return res + l + r

        return check(root,'',0)