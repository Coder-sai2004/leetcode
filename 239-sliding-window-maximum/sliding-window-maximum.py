from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=deque([])
        ans=[]
        #checking the maximum value for the first k window
        for i in range(k):
            while res and nums[i]>res[-1]:
                res.pop()
            res.append(nums[i])

        ans.append(res[0])

        #checking max values for other windows
        for i in range(k,len(nums)):
            if nums[i-k]==res[0]:
                res.popleft()

            #we remove the end elements until the current element is greater than top
            while res and nums[i]>res[-1]:
                res.pop()
            res.append(nums[i])

            #assigning the max value in the window
            ans.append(res[0])
            
        return ans