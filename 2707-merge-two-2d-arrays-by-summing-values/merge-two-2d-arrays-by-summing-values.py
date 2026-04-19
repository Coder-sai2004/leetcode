class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=[]
        j=0
        i=0
        n1,n2=len(nums1),len(nums2)
        while i<n1 or j<n2:
            if i==n1:
                res.append(nums2[j])
                j+=1
            elif j==n2:
                res.append(nums1[i])
                i+=1
            else:
                id1,val1=nums1[i]
                id2,val2=nums2[j]
                if id1==id2:
                    res.append([id1,val1+val2])
                    j+=1
                    i+=1
                elif id1<id2:
                    res.append([id1,val1])
                    i+=1
                elif id1>id2:
                    res.append([id2,val2])
                    j+=1
        return res
