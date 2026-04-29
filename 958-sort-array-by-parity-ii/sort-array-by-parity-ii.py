class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        o=[]
        e=[]
        res=[]
        i=j=k=0
        for x in nums:
            if x%2==0:  e.append(x)
            else:       o.append(x)
        while k<len(nums):
            if k%2==0:
                res.append(e[i])
                i+=1
            else:
                res.append(o[j])
                j+=1
            k+=1
        return res