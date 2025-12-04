class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        a=sorted(nums1)
        b=sorted(nums2)
        i,j=0,0
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                x.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return x