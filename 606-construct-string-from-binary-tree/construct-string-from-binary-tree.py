# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []

        def traverse(node):
            if node is None:
                return
            
            # Add current node
            result.append('(')
            result.append(str(node.val))

            # Preserve empty left child
            if node.left is None and node.right is not None:
                result.append('()')

            traverse(node.left)
            traverse(node.right)
            result.append(')')

        traverse(root)

        # Remove outermost parentheses
        return "".join(result)[1:-1]