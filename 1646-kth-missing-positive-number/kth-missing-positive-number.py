class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]
        s=set(arr)
        for i in range(1,2001):
            if i not in s:
                res.append(i)
        return res[k-1]