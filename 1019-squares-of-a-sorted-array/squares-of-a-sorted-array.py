class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        z=[]
        for i in nums:
            z.append(i**2)
        return sorted(z)