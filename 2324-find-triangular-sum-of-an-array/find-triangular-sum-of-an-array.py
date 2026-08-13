class Solution:
    def add(self,arr):
        temp=[]
        for i in range(1,len(arr)):
            temp.append((arr[i]+arr[i-1])%10)
        return temp
    def triangularSum(self, nums: List[int]) -> int:
        res=nums
        while len(res)!=1:
            res=self.add(res)
        return res[0]