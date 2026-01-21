class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]
        for n in nums:
            val=0
            #converting the n into binary
            ans=list(bin(n)[2:])[::-1]
            s=set(ans)
            #if n==2 it will -1 since it does not have the smallest positive number that
            #satisfies the condition
            if n==2:
                val=-1
            #if 0 in bits then we replace the bits with 1 into 0
            elif '0' in s:
                for i in range(len(ans)-1):
                    if ans[i]=='1' and ans[i+1]=='0':
                        ans[i]='0'
                        val=int("".join(ans[::-1]),2)
                        break
            #if all binary bits are 1's then we remove 1 bit and store that value
            else:
                ans=ans[1:]
                val=int("".join(ans[::-1]),2)
            res.append(val)
        return res