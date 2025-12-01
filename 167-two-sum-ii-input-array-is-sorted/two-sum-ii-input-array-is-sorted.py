class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x=numbers
        l,r=0,len(x)-1
        while l<r:
            sum=x[l]+x[r]
            if sum==target:
                return l+1,r+1
            elif sum<target:
                l+=1
            else:
                r-=1
        return -1