class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        x=len(nums[0])
        n=2**x
        res={int(i,2) for i in nums}
        for i in range(n):
            if i not in res:
                ans=bin(i)[2:]
                return ans.zfill(x)