class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]
        for n in nums:
            val=-1
            ans=0
            b=True
            while ans<n:
                if (ans | (ans+1))==n:
                    val=ans
                    res.append(val)
                    b=False
                    break
                ans+=1
            if b:
                    res.append(val)
        return res