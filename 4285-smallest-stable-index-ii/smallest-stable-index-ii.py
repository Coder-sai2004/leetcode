class Solution(object):
    def firstStableIndex(self, nums, k):
        #initialize mx and mi to store max and min values at the current index
        mx = []
        mi = []
        n = len(nums)
        
        #l is used to store max value while r is used to store min value
        l = 0
        r = float('inf')
        for i in range(n):
            l = max(l,nums[i])
            r = min(r,nums[n-i-1])
            mx.append(l)
            mi.append(r)
        
        #reversing the mi because we are appending from front,but we want min values from end
        mi = mi[::-1]

        #calculation of smallest stable index where the instability score becomes <= k
        for i in range(n):
            if mx[i] - mi[i] <= k:
                return i
        return -1