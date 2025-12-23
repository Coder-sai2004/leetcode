class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(path,start):
            result.append(path.copy())
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(path,i+1)
                path.pop()
        backtrack([],0)
        result=[sorted(i) for i in result]
        sub=[]
        for i in result:
            if i not in sub:
                sub.append(i)
        sub=sorted(sub,key=tuple)
        return sub