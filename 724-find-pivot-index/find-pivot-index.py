class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        x=[]
        x=[nums[0]]
        for i in range(1,len(nums)):
            y=x[i-1]+nums[i]
            x.append(y)
        for i in range(len(x)):
            leftsum=x[i-1]
            rightsum=x[len(x)-1]-x[i]
            if i==0:
                leftsum=0
            if i==len(x)-1:
                rightsum=0
            if leftsum==rightsum:
                return i
        return -1