class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        arr=sorted(satisfaction)
        l=[]
        for i in range(len(arr)):
            res=0
            k=1
            for j in range(i,len(arr)):
                res+=arr[j]*k
                k+=1
            l.append(res)
        r=max(l)
        return max(0,r)