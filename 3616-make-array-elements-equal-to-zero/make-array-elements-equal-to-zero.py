class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        x=[]
        temp=[]
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]==0:
                x.append(i)
        for j in range(len(x)):
            for d in [1,-1]:
                curr=x[j]
                temp=nums.copy()
                direction=d
                while 0<=curr<n:
                    if temp[curr]==0:
                        curr+=direction
                    elif temp[curr]>0:
                        temp[curr]-=1
                        direction*=-1
                        curr+=direction
                if all(z==0 for z in temp):
                    c+=1
        return c