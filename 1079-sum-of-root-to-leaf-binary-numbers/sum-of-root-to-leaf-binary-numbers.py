# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        res = []
        ans = 0
        
        def check(node,s):
            if node is None:
                return -1000000

            if node.left is None and node.right is None:
                s += str(node.val)
                res.append(s)


            l = check(node.left,s + str(node.val))
            r = check(node.right,s + str(node.val))

        check(root,'')
        
        for ch in res:
            ans += int(ch,2)
        return ans