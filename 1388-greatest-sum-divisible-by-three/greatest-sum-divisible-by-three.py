class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        x=sum(nums)
        y=x
        m=x%3
        r=[]
        if m==0:
            return x
        l=sorted(nums)
        for i in l:
            if i>=0 and i%3!=0:
                x-=i
                if x%3==0:
                    r.append(x)
        for i in l:
            if i>=m and i%3!=0:
                y-=i
                if y%3==0:
                    print(y)
                    r.append(y)
                    y+=i
                else:
                    y+=i
        if not r:
            return 0
        return max(r)