class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        r=[]
        for i in range(len(nums)):
            if nums[i]==1:
                r.append(i)
        for j in range(len(r)-1):
            if abs(r[j]-r[j+1])<=k:
                return False
        return True