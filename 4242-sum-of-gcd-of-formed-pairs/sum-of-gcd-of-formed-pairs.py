class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def gcdSum(self, nums: list[int]) -> int:
        res=[]
        mx=0
        ans=0
        for i in range(len(nums)):
            mx=max(nums[i],mx)
            val=self.gcd(mx,nums[i])
            res.append(val)
        res.sort()
        i=0
        j=len(nums)-1
        while i<j:
            v=self.gcd(res[i],res[j])
            ans+=v
            i+=1
            j-=1
        return ans