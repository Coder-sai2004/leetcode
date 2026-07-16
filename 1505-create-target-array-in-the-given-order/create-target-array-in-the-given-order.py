class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=-1
        res=[]
        for i in range(len(nums)):
            if index[i]>n:
                res.append(nums[i])
                n+=1
            else:
                res.insert(index[i],nums[i])
                n+=1
        return res