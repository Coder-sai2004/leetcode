class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #base case checking that nums contains only 1 value or not
        if len(nums)<=1:
            return nums
        
        #mid calculating for dividing of array
        mid=len(nums)//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return self.merge(left,right)

        #conquering the divided elements by sorting
    def merge(self,left,right):
        i=j=0
        res=[]
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res