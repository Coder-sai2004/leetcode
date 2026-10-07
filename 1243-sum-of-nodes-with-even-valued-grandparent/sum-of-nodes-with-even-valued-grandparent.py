# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        values = []

        def traverse(node):
            if node is None:
                return 

            # Check children of even-valued node
            if node.val % 2 == 0:
                
                if node.left:
                    left_left = node.left.left.val if node.left.left else 0
                    left_right = node.left.right.val if node.left.right else 0
                    values.extend([left_left, left_right])
                
                if node.right:
                    right_left = node.right.left.val if node.right.left else 0
                    right_right = node.right.right.val if node.right.right else 0
                    values.extend([right_left, right_right])

            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return sum(values)

        # #this is the code given by chatgpt
        # def dfs(node, parent, grandparent):
        #     if not node:
        #         return 0
        #     return (node.val if grandparent and grandparent.val % 2 == 0 else 0) + \
        #            dfs(node.left, node, parent) + dfs(node.right, node, parent)

        # return dfs(root, None, None)