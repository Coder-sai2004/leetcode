class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=[nums[0]]
        s={}
        c=0
        
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])
        c+=pre.count(k)

        for i in range(len(pre)):
            x=pre[i]-k

            if pre[i]>=k and abs(x) in s:
                c+=s[abs(x)]

            elif pre[i]<k and x in s:
                c+=s[x]

            s[pre[i]]=s.get(pre[i],0)+1
        return c