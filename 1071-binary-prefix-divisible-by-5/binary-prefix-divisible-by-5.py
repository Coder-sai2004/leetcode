class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        r=[]
        s=''
        for i in range(len(nums)):
            s+=str(nums[i])
            res.append(int(s,2))
        for i in res:
            if i%5==0:
                r.append(True)
            else:
                r.append(False)
        return r