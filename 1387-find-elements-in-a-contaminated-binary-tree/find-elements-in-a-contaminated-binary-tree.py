# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode | None):
        self.mx = set()

        def check(root,index):
            if root is None:
                return 0
            
            self.mx.add(index)

            l = check(root.left,(2*index + 1))
            r = check(root.right,(2*index + 2))

        check(root,0)
        
    def find(self, target: int) -> bool:
        if target in self.mx:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)