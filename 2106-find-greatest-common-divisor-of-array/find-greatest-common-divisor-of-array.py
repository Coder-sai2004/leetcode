class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        for i in range(y,0,-1):
            if x%i==0 and y%i==0:
                return i