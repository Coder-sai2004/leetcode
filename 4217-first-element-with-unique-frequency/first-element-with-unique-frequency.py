from collections import Counter
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq=Counter(nums)
        v=list(freq.values())
        unique_freq=Counter(v)
        for i in nums:
            a=freq[i]
            u=unique_freq[a]
            if u==1:
                return i
        return -1