class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1,n2=[],[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                n1.append(i)
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                n2.append(j)
        if len(n1)==0 or len(n2)==0:
            return [0,0]
        return [len(n1),len(n2)]