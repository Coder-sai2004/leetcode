class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        temp=[]
        for n in nums:
            while n>0:
                temp.append(n%10)
                n//=10
            ans.extend(temp[::-1])
            temp=[]
        return ans