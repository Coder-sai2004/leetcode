from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #taking counter of nums for frequencies
        x=Counter(nums)

        #sorting the values based on frequency by high to low
        y=sorted(x.items(),key=lambda x: x[1], reverse=True)
        
        #taking first values of y upto k
        res=[nums for nums,freq in y[:k]]
        return res