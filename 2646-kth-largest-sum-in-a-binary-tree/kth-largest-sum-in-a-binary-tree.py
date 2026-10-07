# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        level_sums = []
        
        def traverse(node, depth):
            if node is None:
                return 

            # Initialize level sum
            if len(level_sums) <= depth:
                level_sums.append(0)
            
            level_sums[depth] += node.val

            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)

        traverse(root, 0)

        # Sort and get kth largest
        if len(level_sums) < k:
            return -1
        level_sums.sort()
        return level_sums[-k]