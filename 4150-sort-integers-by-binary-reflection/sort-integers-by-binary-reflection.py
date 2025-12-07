import heapq
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        r,y,heap=[],[],[]
        for i in nums:
            r.append(int(bin(i)[2:][::-1],2))
        for j in range(len(nums)):
            heapq.heappush(heap,(r[j],nums[j]))
        heap=sorted(heap)
        for k in range(len(nums)):
            y.append(heap[k][1])
        return y