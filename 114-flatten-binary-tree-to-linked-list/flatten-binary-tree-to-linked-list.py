# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        st = []
        def check(root):
            if root is None:
                return 
        
            if root.left and root.right:
                st.append(root.right)
                root.right = root.left
                root.left = None

            elif root.left:
                root.right = root.left
                root.left = None

            if root.left is None and root.right is None and st:
                x = st.pop()
                root.right = x
                
            check(root.right)

        check(root)