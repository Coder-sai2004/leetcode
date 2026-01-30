class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        exp=1
        n=len(nums)
        mx=max(nums)
        radix=[[],[],[],[],[],[],[],[],[],[]]
        while mx//exp>0:
            for _ in range(n):
                val=nums.pop()
                idx=(val//exp)%10
                radix[idx].append(val)

            for bucket in radix:
                while len(bucket)>0:
                    val=bucket.pop()
                    nums.append(val)
            exp*=10
        m=0
        for i in range(len(nums)-1):
            m=max(m,abs(nums[i]-nums[i+1]))
        return m