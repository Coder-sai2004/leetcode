class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        #initialization
        s=set(nums)
        res=[]
        freq={}
        ans=[]

        #creating subarrays of size k
        for i in range(k,len(nums)+1):
            res.append(nums[i-k:i])
        
        #finding the number of times an element appeared in subarray
        for num in s:
            for sub in res:
                if num in sub:
                    if num in freq:
                        freq[num]+=1
                    else:
                        freq[num]=1
        
        #taking the elements where it only appeared in one subarray
        for key,val in freq.items():
            if val==1:
                ans.append(key)
                
        #returning the largest almost missing integer
        if ans:
            return max(ans)
        return -1