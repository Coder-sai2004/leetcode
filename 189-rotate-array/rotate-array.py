class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m=k%len(nums)
        l=len(nums)-m
        a=nums[:l]
        b=nums[l:]
        nums[:]=b+a