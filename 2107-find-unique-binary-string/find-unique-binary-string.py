class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        x=len(nums[0])
        n=2**x
        arr=[bin(i)[2:] for i in range(n)]
        res=[i.zfill(x) for i in arr]
        s=set(nums)
        for i in res:
            if i not in s:
                return i