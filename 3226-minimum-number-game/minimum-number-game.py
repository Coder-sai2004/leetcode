import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []
        heapq.heapify(nums)
        while nums:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            res.append(b)
            res.append(a)
        return res