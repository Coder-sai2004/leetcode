class Solution:
    def hIndex(self, citations: List[int]) -> int:
        x=citations
        res=[]
        arr=sorted(x,reverse=True)
        c=0
        i=0
        k=len(arr)
        while i<len(arr):
            if k<=arr[i]:
                c+=1
            else:
                if k<=c:
                    res.append(k)
                i-=1
                k-=1
            i+=1
        if k<=c:
            res.append(k)
        return max(res)