class Solution:
    def check(self, nums , idx):
        #edge case if idx is 0
        if idx == 0:
            i = 1
            j = 2
        else:
            i = 0
            j = 1

        while j < len(nums):
            #skipping (means removing one element to check if array is strictly increasing)
            if j == idx:
                j += 1
                continue
            
            #after skipping element ,even then also it is not increasing then we cannot make it increasing
            if nums[i] >= nums[j]:
                return False

            #after skipping one element,we need to get difference between i and j into 1,because we need to compare adjacent elements    
            if j - i == 1:
                i += 1
            else:
                i = j
            
            j += 1
            
        return True
    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(1,len(nums)):
            #when the previous element is greater than current element
            if nums[i-1] >= nums[i]:
                return (self.check(nums , i - 1)) or (self.check(nums , i))
        
        return True