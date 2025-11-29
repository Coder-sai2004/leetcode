class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=set(nums)
        y=list(x)
        cou={}
        c=[]
        for i in range(len(y)):
            cou[y[i]]=nums.count(y[i])
        for i,j in cou.items():
            if j>=2:
                c.append(i)
                c.append(i)
            else:
                c.append(i)
        nums[:]=sorted(c)
        return len(nums)