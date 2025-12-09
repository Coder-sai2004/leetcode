import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        x=list(itertools.permutations(nums))
        return x