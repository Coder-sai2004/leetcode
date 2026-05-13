class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=[-1]*n
        i=0
        m=(n*2)-1
        j=0
        while i<n:
            while stack and nums[stack[-1]]<nums[i]:
                idx=stack.pop()
                res[idx]=nums[i]
            stack.append(i)
            i+=1
            i=i%n
            j+=1
            if j==m:
                break
        return res