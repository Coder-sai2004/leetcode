class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        window=2*k
        x=[]
        a=[]
        b=[]
        first=False
        second=True
        n=len(nums)-window+1
        if k==1:
            return True
        for i in range(n):
            a=nums[i:k]
            for c in range(len(a)-1):
                if a[c]<a[c+1]:
                    first=True
                else:
                    first=False
                    break
            b=nums[k:window]
            for d in range(len(b)-1):
                if b[d]<b[d+1]:
                    second=True
                else:
                    second=False
                    break
            if first and second:
                return True
            window+=1
            k+=1
        return False