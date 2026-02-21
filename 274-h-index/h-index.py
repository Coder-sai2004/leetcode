class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res=[]
        for i in range(len(citations)+1):
            c=0
            for j in citations:
                if i<=j:
                    c+=1
            if i<=c:
                res.append(i)
        return max(res)