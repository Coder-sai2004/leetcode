class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        l={}
        r={}
        ls=0
        rs=0
        res=[]
        for i in range(len(nums)):
            if nums[i]>ls:
                l[i]=nums[i]
                ls=nums[i]
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>rs:
                r[j]=nums[j]
                rs=nums[j]
        temp=l|r
        s=sorted(temp.items(),key=lambda x: x[0])
        for x in s:
            res.append(x[1])
        return res