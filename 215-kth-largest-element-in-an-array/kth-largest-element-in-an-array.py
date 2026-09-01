import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-i for i in nums]
        heapq.heapify(nums)
        c=1
        while c!=k:
            heapq.heappop(nums)
            c+=1
        return -nums[0]