class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        pre=[nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])
        d={}
        d[0]=-1
        m=0
        for i in range(len(pre)):
            if pre[i] not in d:
                d[pre[i]]=i
            elif pre[i] in d:
                m=max(m,i-d[pre[i]])
        return m