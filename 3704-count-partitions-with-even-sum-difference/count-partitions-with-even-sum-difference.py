class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(1,n):
            a=sum(nums[:i])
            b=sum(nums[i:n])
            if abs(a-b)%2==0:
                c+=1
        return c