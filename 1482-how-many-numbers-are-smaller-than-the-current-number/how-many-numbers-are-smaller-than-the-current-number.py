class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=sorted(nums)
        d={}
        res=[]
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=i   
                
        for i in range(len(nums)):
            res.append(d[nums[i]])
        return res