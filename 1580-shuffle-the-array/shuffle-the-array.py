class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        r=[]
        while j<len(nums):
            r.append(nums[i])
            r.append(nums[j])
            i+=1
            j+=1
        return r