class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #taking prefix sum of nums and s for frequency to calculate the subarrays
        pre=[nums[0]]
        s={}
        c=0
        #calculating the prefix sum of nums
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])
        c+=pre.count(k)

        #here we calculate the difference between current element and k value and check whether it 
        #exists in the hash table and also consider how many times the difference is there to 
        #calculate correct count of subarrays
        for i in range(len(pre)):
            x=pre[i]-k

            if pre[i]>=k and abs(x) in s:
                c+=s[abs(x)]

            elif pre[i]<k and x in s:
                c+=s[x]

            s[pre[i]]=s.get(pre[i],0)+1
            
        return c