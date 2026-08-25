class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        i=1
        val=i*k
        mx=max(nums)
        while val<=mx:
            if val not in s:
                return val
            i+=1
            val=i*k
        return val