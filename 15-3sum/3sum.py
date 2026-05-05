class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            a=i+1
            b=len(nums)-1
            while a<b:
                s=nums[i]+nums[a]+nums[b]
                if s==0:
                    res.append([nums[i],nums[a],nums[b]])
                    a+=1
                    b-=1
                    while a<b and nums[a]==nums[a-1]:
                        a+=1
                    while a<b and nums[b]==nums[b+1]:
                        b-=1
                elif s<0:
                    a+=1
                else:
                    b-=1
        return res