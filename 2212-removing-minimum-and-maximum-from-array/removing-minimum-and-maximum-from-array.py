class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        #identifying min,max values in the nums
        mi=min(nums)
        mx=max(nums)

        #finding index of min,max values
        mi_idx=nums.index(mi)
        mx_idx=nums.index(mx)

        #l refers to smallest index,r refers largest index
        l=min(mi_idx,mx_idx)
        r=max(mi_idx,mx_idx)

        #number of elements need to be delete to remove min,max values of nums from left side
        x=r+1
        #number of elements need to be delete to remove min,max values of nums from right side
        y=n-l
        #number of elements need to be delete to remove min,max values of nums from both ends
        z=(l+1)+(n-r)

        #returning the smallest number of elements need to delete to remove min,max values from the nums
        return min(x,y,z)