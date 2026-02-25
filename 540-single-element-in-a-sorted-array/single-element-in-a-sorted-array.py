class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if (m==0 and nums[m]!=nums[m+1]) or (m==n-1 and nums[m]!=nums[m-1]) or (nums[m]!=nums[m+1] and nums[m]!=nums[m-1] and m!=0 and m!=n-1):
                return nums[m]
            elif nums[m]==nums[m-1] and m!=0:
                if m%2==1:
                    l=m+1
                else:
                    h=m-1
            elif nums[m]==nums[m+1] and m!=n-1:
                if m%2==0:
                    l=m+1
                else:
                    h=m-1