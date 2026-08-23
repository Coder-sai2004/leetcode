class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        s=set(nums)
        res=[]
        ans=[]

        for i in range(lower,upper+1):
            if i not in s:
                res.append(i)

        if len(res)==0:
            return []

        x=res[0]
        y=res[0]
        for j in range(len(res)-1):
            if res[j]+1!=res[j+1]:
                ans.append([x,y])
                x=res[j+1]
                y=res[j+1]
            else:
                y=res[j+1]
        ans.append([x,y])
        
        return ans