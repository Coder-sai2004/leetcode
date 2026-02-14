class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n=len(nums)//2
        i=0
        res=[]
        while i<n:
            a=min(nums)
            b=max(nums)
            res.append((a+b)/2)
            nums.remove(a)
            nums.remove(b)
            i+=1
        return min(res)