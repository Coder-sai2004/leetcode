class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        gains = [int("".join(sorted(str(x),reverse = True))) - x for x in nums]
        gains.sort(reverse = True)
        return sum(nums) + sum(gains[:k])