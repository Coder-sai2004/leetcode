class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result=[]
        def backtrack(path,start):
            result.append(path.copy())
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(path,i+1)
                path.pop()
        backtrack([],0)
        m=0
        c=0
        for i in nums:
            m=m|i
        for num in result:
            if len(num)>0:
                x=0
                for i in num:
                    x=x|i
                if x==m:
                    c+=1
        return c