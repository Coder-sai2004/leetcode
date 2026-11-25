class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = 0
        for val in nums:
            if val < k:
                op += 1
        return op