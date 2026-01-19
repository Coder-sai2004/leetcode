class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            while i%3!=0:
                a=min(i%3,3-(i%3))
                b=max(i%3,3-(i%3))
                c+=min(i%3,3-(i%3))
                if (i+a)%3==0:
                    i+=a
                else:
                    i+=b
        return c