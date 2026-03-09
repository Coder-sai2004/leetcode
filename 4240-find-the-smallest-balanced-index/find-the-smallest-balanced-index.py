class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        if len(nums)==1:
            return -1
        pro=[-1]*len(nums)
        pro[len(nums)-1]=nums[len(nums)-1]
        s=sum(nums)
        for i in range(len(nums)-2,-1,-1):
            if (pro[i+1]*nums[i])>s:
                break
            pro[i]=(pro[i+1]*nums[i])
        left=0
        print(pro)
        for i in range(len(nums)):
            if i==len(nums)-1:
                b=1
            else:
                b=pro[i+1]
            if left==b:
                return i
            left+=nums[i]
        return -1