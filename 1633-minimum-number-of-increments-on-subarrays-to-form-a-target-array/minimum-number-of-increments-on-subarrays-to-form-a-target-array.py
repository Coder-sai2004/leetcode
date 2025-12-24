class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        c=target[0]
        for i in range(len(target)-1):
            if target[i]<target[i+1]:
                c+=target[i+1]-target[i]
        return c