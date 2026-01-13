class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[0]
        r=[0]
        x=nums[::-1]
        n=len(nums)-1
        res=[]
        for i in range(n):
            l.append(nums[i]+l[i])
        for j in range(n):
            r.append(x[j]+r[j])
        r=r[::-1]
        for i in range(len(nums)):
            res.append(abs(l[i]-r[i]))
        return res