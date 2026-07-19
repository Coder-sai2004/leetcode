# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.ans=0
        def post(root):
            if root is None:
                return 0
            left=post(root.left)
            right=post(root.right)
            sub=max(left,right)
            if root.val>=sub:
                self.ans+=1
            return max(root.val,sub)
        post(root)
        return self.ans