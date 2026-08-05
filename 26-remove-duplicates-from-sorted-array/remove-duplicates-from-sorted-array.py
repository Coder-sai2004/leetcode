from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        x=Counter(nums)
        for i in nums:
            f=x[i]
            while f>1:
                nums.remove(i)
                f-=1
        return len(nums)