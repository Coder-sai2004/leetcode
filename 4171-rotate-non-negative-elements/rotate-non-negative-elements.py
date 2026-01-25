class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        res=[]
        i=0
        j=0
        #collecting positive elements for rotation
        for x in nums:
            if x>=0:
                res.append(x)
        #number of rotations we need to make
        if not res:
            return nums
        n=k%len(res)
        res=res[n:]+res[:n]
        #rearranging the order of original array
        while i<len(nums):
            if nums[i]>=0:
                nums[i]=res[j]
                j+=1
            i+=1
        return nums