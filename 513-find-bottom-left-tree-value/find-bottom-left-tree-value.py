# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        leaves = defaultdict(list)

        def traverse(node, depth):
            if node is None:
                return

            # Store leaf values by level
            if node.left is None and node.right is None:
                leaves[depth].append(node.val)

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 1)

        # Return leftmost value at deepest level
        if leaves:
            return leaves[max(leaves.keys())][0]
        else:
            return root.val