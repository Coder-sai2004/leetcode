class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            b=True
            x=nums2.index(i)
            for j in range(x,len(nums2)):
                if i<nums2[j]:
                    res.append(nums2[j])
                    b=False
                    break
            if b:
                res.append(-1)
        return res