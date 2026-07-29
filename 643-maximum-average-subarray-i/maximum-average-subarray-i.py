class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx=0
        mx_avg=-10000
        #taking the first window avgerage for further calculations
        for i in range(k):
            mx+=nums[i]
        mx_avg=max(mx_avg,(mx)/k)
        #calculating next windows averages and taking the maximum average
        for j in range(k,len(nums)):
            mx+=nums[j]
            mx-=nums[j-k]
            mx_avg=max(mx_avg,(mx)/k)
        return mx_avg