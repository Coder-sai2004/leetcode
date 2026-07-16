class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=sorted(nums)
        d={}
        res=[]
        
        for i in range(len(arr)):
            if arr[i]==arr[i-1] and i>0:
                d[arr[i]]=d[arr[i-1]]
            else:
                d[arr[i]]=i

        for i in range(len(nums)):
            res.append(d[nums[i]])
        return res