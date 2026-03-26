class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        o=[]
        e=[]
        for i in nums:
            if i%2==0:  e.append(i)
            else:       o.append(i)
        return e+o